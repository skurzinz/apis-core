from django.db import models
#from reversion import revisions as reversion
import reversion
from django.db.models import Q
import operator
import pdb

from apis_core.apis_entities.models import Person, Place, Institution, Event, Passage, Publication
from apis_core.apis_metainfo.models import TempEntityClass
from apis_core.apis_vocabularies.models import (PersonPersonRelation, PersonPlaceRelation,
    PersonInstitutionRelation, PersonEventRelation, PersonPassageRelation, PersonPublicationRelation,
    InstitutionInstitutionRelation, InstitutionEventRelation, InstitutionPlaceRelation,
    InstitutionPassageRelation, InstitutionPublicationRelation, PlacePlaceRelation, PlaceEventRelation,
    PlacePassageRelation, PlacePublicationRelation, EventEventRelation, EventPassageRelation,
    EventPublicationRelation, PassagePassageRelation, PassagePublicationRelation, PublicationPublicationRelation)


#######################################################################
#
# Custom Managers
#
#######################################################################


class AnnotationRelationLinkManager(models.Manager):
    """Manager used to retrieve only those relations that are highlighted in the texts.
    Reads out the ``annotation_project`` and ``users_show_highlighter`` session variables and provides a filter.
    Needs a :class:`django.request` object in order to read out the ``session`` variable.

    *Example:*
    ::

        relation = PersonPlace.objects.filter(related_place='Wien').filter_ann_project(request=request)

    Returns only those relations that are connected with an annotation that fits the session variables or are not
    connected to any annotation at all.
    """
    def filter_ann_proj(self, request=None, ann_proj=1, include_all=True):
        """The filter function provided by the manager class.

        :param request: `django.request` object
        :return: queryset that contains only objects that are shown in the highlighted text or those not connected
            to an annotation at all.
        """
        users_show = None
        if request:
            ann_proj = request.session.get('annotation_project', 1)
            if not ann_proj:
                ann_proj = 1
            users_show = request.session.get('users_show_highlighter', None)
        query = Q(annotation__annotation_project_id=ann_proj)
        qs = super(AnnotationRelationLinkManager, self).get_queryset()
        if users_show is not None:
            query.add(Q(annotation__user_added_id__in=users_show), Q.AND)
        if include_all:
            query.add(Q(annotation__annotation_project__isnull=True), Q.OR)
        return qs.filter(query)



#######################################################################
#
# Person - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class PersonPerson(TempEntityClass):
    """Defines and describes a relation between a Person and another Person

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PersonPersonRelation`
    :param int related_personA: Foreign Key to :class:`entities.models.Person`
    :param int related_personB: Foreign Key to :class:`entities.models.Person`
    """

    relation_type = models.ForeignKey(PersonPersonRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_personA = models.ForeignKey(
        Person, blank=True, null=True, related_name="related_personA",
        on_delete=models.CASCADE)
    related_personB = models.ForeignKey(
        Person, blank=True, null=True, related_name="related_personB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_personA, self.relation_type, self.related_personB)

    def get_web_object(self):
        """Used in some html views.

        :return: Dict with object properties
        """
        if self.related_personA.first_name is None:
            self.related_personA.first_name = '-'
        if self.related_personB.first_name is None:
            self.related_personB.first_name = '-'
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_personA': self.related_personA.name+', '+self.related_personA.first_name,
            'related_personB': self.related_personB.name+', '+self.related_personB.first_name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        """
        Function that returns dict used in relation tables.

        :param entity: :class:`entities.models.Person` instance that is the starting point of the table.
        :return: dict
        """
        if self.related_personA == entity:
            rel_pers = self.related_personB
            rel_type = self.relation_type.name
        elif self.related_personB == entity:
            rel_pers = self.related_personA
            rel_type = self.relation_type.name_reverse
        result = {
            'pk': self.pk,
            'relation_type': rel_type,
            'related_person': rel_pers,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PersonPlace(TempEntityClass):
    """Defines and describes a relation between a Person and a Place

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PersonPlaceRelation`
    :param int related_person: Foreign Key to :class:`entities.models.Person`
    :param int related_place: Foreign Key to :class:`entities.models.Place`
    """

    relation_type = models.ForeignKey(PersonPlaceRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_person = models.ForeignKey(
        Person, blank=True, null=True, on_delete=models.CASCADE)
    related_place = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_person, self.relation_type, self.related_place)

    def get_web_object(self):
        """Used in some html views.

        :return: Dict with object properties
        """

        if self.related_person.first_name is None:
            self.related_person.first_name = '-'
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_person': self.related_person.name+', '+self.related_person.first_name,
            'related_place': self.related_place.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PersonInstitution(TempEntityClass):
    """ Defines and describes a relation between a Person and a Institution

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PersonInstitutionRelation`
    :param int related_person: Foreign Key to :class:`entities.models.Person`
    :param int related_institution: Foreign Key to :class:`entities.models.Institution`
    """

    relation_type = models.ForeignKey(PersonInstitutionRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_person = models.ForeignKey(
        Person, blank=True, null=True, on_delete=models.CASCADE)
    related_institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_person, self.relation_type, self.related_institution)

    def get_web_object(self):

        if self.related_person.first_name is None:
            self.related_person.first_name = '-'
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_person': self.related_person.name+', '+self.related_person.first_name,
            'related_institution': self.related_institution.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PersonEvent(TempEntityClass):
    """ Defines and describes a relation bewteen a Person and an Event

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PersonEventRelation`
    :param int related_person: Foreign Key to :class:`entities.models.Person`
    :param int related_event: Foreign Key to :class:`entities.models.Event`
    """

    relation_type = models.ForeignKey(PersonEventRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_person = models.ForeignKey(
        Person, blank=True, null=True, on_delete=models.CASCADE)
    related_event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_person, self.relation_type, self.related_event)

    def get_web_object(self):

        if self.related_person.first_name is None:
            self.related_person.first_name = '-'
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_person': self.related_person.name+', '+self.related_person.first_name,
            'related_event': self.related_event.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PersonPassage(TempEntityClass):
    """ Defines and describes a relation between a Person and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PersonPassageRelation`
    :param int related_person: Foreign Key to :class:`entities.models.Person`
    :param int related_passage: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(PersonPassageRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_person = models.ForeignKey(
        Person, blank=True, null=True, on_delete=models.CASCADE)
    related_passage = models.ForeignKey(
        Passage, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_person, self.relation_type, self.related_passage)

    def get_web_object(self):

        if self.related_person.first_name is None:
            self.related_person.first_name = '-'
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_person': self.related_person.name+', '+self.related_person.first_name,
            'related_passage': self.related_passage.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PersonPublication(TempEntityClass):
    """ Defines and describes a relation between a Person and a Publication

    :param int relation_type: Foreign Key to :class: vocabularies.models.PersonPublicationRelation
    :param int related_person: Forein Key to :class: `entities.models.Person`
    :param int related_publication: Forein Key to :class: `entities.models.Publication`
    """

    relation_type = models.ForeignKey(PersonPublicationRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_person = models.ForeignKey(
        Person, blank=True, null=True, on_delete=models.CASCADE)
    related_publication = models.ForeignKey(
        Publication, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_person, self.relation_type, self.related_publication)

    def get_web_object(self):

        if self.related_person.first_name is None:
            self.related_person.first_name = '-'
        result = {
            'relation_ok': self.pk,
            'relation_type': self.relation_type.name,
            'related_person': self.related_person.name+', '+self.related_person.first_name,
            'related_publication': self.related_publication.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result



#######################################################################
#
#   Institution - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class InstitutionInstitution(TempEntityClass):
    """ Defines and describes a relation between two Institutions

    :param int relation_type: Foreign Key to :class:`vocabularies.models.InstitutionInstitutionRelation`
    :param int related_institutionA: Foreign Key to :class:`entities.models.Institution`
    :param int related_institutionB: Foreign Key to :class:`entities.models.Institution`
    """

    relation_type = models.ForeignKey(InstitutionInstitutionRelation,
                                      blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_institutionA = models.ForeignKey(
        Institution, blank=True, null=True, related_name="related_institutionA",
        on_delete=models.CASCADE)
    related_institutionB = models.ForeignKey(
        Institution, blank=True, null=True, related_name="related_institutionB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_institutionA, self.relation_type, self.related_institutionB)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_institutionA': self.related_institutionA.name,
            'related_institutionB': self.related_institutionB.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        if self.related_institutionA == entity:
            rel_inst = self.related_institutionB
            rel_type = self.relation_type.name
        elif self.related_institutionB == entity:
            rel_inst = self.related_institutionA
            rel_type = self.relation_type.name_reverse
        result = {
            'relation_pk': self.pk,
            'relation_type': rel_type,
            'related_institution': rel_inst,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class InstitutionPlace(TempEntityClass):
    """Describes a relation bewteen an Institution  and a Place

    :param int relation_type: Foreign Key to :class:`vocabularies.models.InstitutionPlaceRelation`
    :param int related_institution: Foreign Key to :class:`entities.models.Institution`
    :param int related_place: Foreign Key to :class:`entities.models.Place`
    """

    relation_type = models.ForeignKey(
        InstitutionPlaceRelation, blank=True, null=True,
        on_delete=models.SET_NULL)
    related_institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    related_place = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_institution, self.relation_type, self.related_place)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_institution': self.related_institution.name,
            'related_place': self.related_place.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class InstitutionEvent(TempEntityClass):
    """Describes a relation bewteen an Institution and an Event

    :param int relation_type: Foreign Key to :class:`vocabularies.models.InstitutionEventRelation`
    :param int related_institution: Foreign Key to :class:`entities.models.Institution`
    :param int related_event: Foreign Key to :class:`entities.models.Event`
    """

    relation_type = models.ForeignKey(InstitutionEventRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    related_event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_institution, self.relation_type, self.related_event)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_institution': self.related_institution.name,
            'related_event': self.related_event.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class InstitutionPassage(TempEntityClass):
    """Describes a relation bewteen an Institution and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.InstitutionPassageRelation`
    :param int related_institution: Foreign Key to :class:`entities.models.Institution`
    :param int related_passage: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(InstitutionPassageRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    related_passage = models.ForeignKey(
        Passage, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_institution, self.relation_type, self.related_passage)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_institution': self.related_institution.name,
            'related_passage': self.related_passage.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class InstitutionPublication(TempEntityClass):
    """Describes a relation bewteen an Institution and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.InstitutionPassageRelation`
    :param int related_institution: Foreign Key to :class:`entities.models.Institution`
    :param int related_passage: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(InstitutionPublicationRelation, blank=True,
                                      null=True, on_delete=models.SET_NULL)
    related_institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.CASCADE)
    related_publication = models.ForeignKey(
        Publication, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_institution, self.relation_type, self.related_publication)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_institution': self.related_institution.name,
            'related_publication': self.related_publication.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result



#######################################################################
#
#   Place - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class PlacePlace(TempEntityClass):
    """Describes a relation bewteen an Place  and a Place

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PlacePlaceRelation`
    :param int related_placeA: Foreign Key to :class:`entities.models.Place`
    :param int related_placeB: Foreign Key to :class:`entities.models.Place`
    """

    relation_type = models.ForeignKey(PlacePlaceRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_placeA = models.ForeignKey(
        Place, blank=True, null=True, related_name="related_placeA",
        on_delete=models.CASCADE)
    related_placeB = models.ForeignKey(
        Place, blank=True, null=True, related_name="related_placeB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_placeA, self.relation_type, self.related_placeB)

    def get_web_object(self):
        """Used in some html views.

        :return: Dict with object properties
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_placeA': self.related_placeA.name,
            'related_placeB': self.related_placeB.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        """Dict for the tabels in the html view

        :param entity: Object of type :class:`entities.models.Place`; Used to determine which Place is the main entity
            and which one the related.
        :return:
        """
        if self.related_placeA == entity:
            rel_place = self.related_placeB
            rel_type = self.relation_type.name
        elif self.related_placeB == entity:
            rel_place = self.related_placeA
            rel_type = self.relation_type.name_reverse
        result = {
            'relation_pk': self.pk,
            'relation_type': rel_type,
            'related_place': rel_place,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PlaceEvent(TempEntityClass):
    """Describes a relation between an Place and an Event

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PlaceEventRelation`
    :param int related_place: Foreign Key to :class:`entities.models.Place`
    :param int related_event: Foreign Key to :class:`entities.models.Event`
    """

    relation_type = models.ForeignKey(PlaceEventRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_place = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.CASCADE)
    related_event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_place, self.relation_type, self.related_event)

    def get_web_object(self):
        """Function that returns a dict that is used in html views.

        :return: dict of attributes
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_place': self.related_place.name,
            'related_event': self.related_event.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PlacePassage(TempEntityClass):
    """Describes a relation between an Place and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PlacePassageRelation`
    :param int related_place: Foreign Key to :class:`entities.models.Place`
    :param int related_Passage: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(PlacePassageRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_place = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.CASCADE)
    related_passage = models.ForeignKey(
        Passage, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_place, self.relation_type, self.related_passage)

    def get_web_object(self):
        """Function that returns a dict that is used in html views.

        :return: dict of attributes
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_place': self.related_place.name,
            'related_passage': self.related_passage.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result
    

@reversion.register(follow=['tempentityclass_ptr'])
class PlacePublication(TempEntityClass):
    """Describes a relation between an Place and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PlacePublicationRelation`
    :param int related_place: Foreign Key to :class:`entities.models.Place`
    :param int related_Publication: Foreign Key to :class:`entities.models.Publication`
    """

    relation_type = models.ForeignKey(PlacePublicationRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_place = models.ForeignKey(
        Place, blank=True, null=True, on_delete=models.CASCADE)
    related_publication = models.ForeignKey(
        Publication, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_place, self.relation_type, self.related_publication)

    def get_web_object(self):
        """Function that returns a dict that is used in html views.

        :return: dict of attributes
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_place': self.related_place.name,
            'related_publication': self.related_publication.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result



#######################################################################
#
#   Event - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class EventEvent(TempEntityClass):
    """Describes a relation between an Event and an Event

    :param int relation_type: Foreign Key to :class:`vocabularies.models.EventEventRelation`
    :param int related_eventA: Foreign Key to :class:`entities.models.Event`
    :param int related_eventB: Foreign Key to :class:`entities.models.Event`
    """

    relation_type = models.ForeignKey(EventEventRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_eventA = models.ForeignKey(
        Event, blank=True, null=True, related_name="related_eventA",
        on_delete=models.CASCADE)
    related_eventB = models.ForeignKey(
        Event, blank=True, null=True, related_name="related_eventB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_eventA, self.relation_type, self.related_eventB)

    def get_web_object(self):
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_eventA': self.related_eventA.name,
            'related_eventB': self.related_eventB.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        if self.related_eventA == entity:
            rel_event = self.related_eventB
            rel_type = self.relation_type.name
        elif self.related_eventB == entity:
            rel_event = self.related_eventA
            rel_type = self.relation_type.name_reverse
        result = {
            'relation_pk': self.pk,
            'relation_type': rel_type,
            'related_event': rel_event,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class EventPassage(TempEntityClass):
    """Describes a relation between an Event and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.EventPassageRelation`
    :param int related_event: Foreign Key to :class:`entities.models.Event`
    :param int related_passage: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(EventPassageRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    related_passage = models.ForeignKey(
        Passage, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_event, self.relation_type, self.related_passage)

    def get_web_object(self):
        """Function that returns a dict that is used in html views.

        :return: dict of attributes
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_event': self.related_event.name,
            'related_passage': self.related_passage.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class EventPublication(TempEntityClass):
    """ Defines and describes a relation between a Event and a Publication

    :param int relation_type: Foreign Key to :class: vocabularies.models.EventPublicationRelation
    :param int related_event: Forein Key to :class: `entities.models.Event`
    :param int related_publication: Forein Key to :class: `entities.models.Publication`
    """

    relation_type = models.ForeignKey(EventPublicationRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_event = models.ForeignKey(
        Event, blank=True, null=True, on_delete=models.CASCADE)
    related_publication = models.ForeignKey(
        Publication, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_event, self.relation_type, self.related_publication)

    def get_web_object(self):

        result = {
            'relation_ok': self.pk,
            'relation_type': self.relation_type.name,
            'related_event': self.related_event.name,
            'related_publication': self.related_publication.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result



#######################################################################
#
#   Passage - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class PassagePassage(TempEntityClass):
    """Describes a relation between an Passage and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PassagePassageRelation`
    :param int related_passageA: Foreign Key to :class:`entities.models.Passage`
    :param int related_passageB: Foreign Key to :class:`entities.models.Passage`
    """

    relation_type = models.ForeignKey(PassagePassageRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_passageA = models.ForeignKey(
        Passage, blank=True, null=True, related_name="related_passageA",
        on_delete=models.CASCADE)
    related_passageB = models.ForeignKey(
        Passage, blank=True, null=True, related_name="related_passageB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_passageA, self.relation_type, self.related_passageB)

    def get_web_object(self):
        """Used in some html views.

        :return: Dict with object properties
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_passageA': self.related_passageA.name,
            'related_passageB': self.related_passageB.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        """Dict for the tabels in the html view

        :param entity: Object of type :class:`entities.models.Place`; Used to determine which Place is the main entity
            and which one the related.
        :return:
        """
        if self.related_passageA == entity:
            rel_passage = self.related_passageB
            rel_type = self.relation_type.name
        elif self.related_passageB == entity:
            rel_passage = self.related_passageA
            rel_type = self.relation_type.name_reverse
        result = {
            'relation_pk': self.pk,
            'relation_type': rel_type,
            'related_passage': rel_passage,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


@reversion.register(follow=['tempentityclass_ptr'])
class PassagePublication(TempEntityClass):
    """Describes a relation between an Place and a Passage

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PassagePublicationRelation`
    :param int related_passage: Foreign Key to :class:`entities.models.Passage`
    :param int related_Publication: Foreign Key to :class:`entities.models.Publication`
    """
    
    relation_type = models.ForeignKey(PassagePublicationRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_passage = models.ForeignKey(
        Passage, blank=True, null=True, on_delete=models.CASCADE)
    related_publication = models.ForeignKey(
        Publication, blank=True, null=True, on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(
            self.related_passage, self.relation_type, self.related_publication)

    def get_web_object(self):
        """Function that returns a dict that is used in html views.

        :return: dict of attributes
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_passage': self.related_passage.name,
            'related_publication': self.related_publication.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result
    


#######################################################################
#
#   Publication - ... - Relation
#
#######################################################################


@reversion.register(follow=['tempentityclass_ptr'])
class PublicationPublication(TempEntityClass):
    """Describes a relation bewteen an Place  and a Place

    :param int relation_type: Foreign Key to :class:`vocabularies.models.PublicationPublicationRelation`
    :param int related_publicationA: Foreign Key to :class:`entities.models.Publication`
    :param int related_publicationB: Foreign Key to :class:`entities.models.Publication`
    """
    
    relation_type = models.ForeignKey(PublicationPublicationRelation, blank=True, null=True,
                                      on_delete=models.SET_NULL)
    related_publicationA = models.ForeignKey(
        Publication, blank=True, null=True, related_name="related_publicationA",
        on_delete=models.CASCADE)
    related_publicationB = models.ForeignKey(
        Publication, blank=True, null=True, related_name="related_publicationB",
        on_delete=models.CASCADE)
    objects = models.Manager()
    annotation_links = AnnotationRelationLinkManager()

    def __str__(self):
        return "{} ({}) {}".format(self.related_publicationA, self.relation_type, self.related_publicationB)

    def get_web_object(self):
        """Used in some html views.

        :return: Dict with object properties
        """
        result = {
            'relation_pk': self.pk,
            'relation_type': self.relation_type.name,
            'related_publicationA': self.related_publicationA.name,
            'related_publicationB': self.related_publicationB.name,
            'start_date': self.start_date_written,
            'end_date': self.end_date_written}
        return result

    def get_table_dict(self, entity):
        """Dict for the tabels in the html view

        :param entity: Object of type :class:`entities.models.Place`; Used to determine which Publication is the main entity
            and which one the related.
        :return:
        """
        if self.related_publicationA == entity:
            rel_publication = self.related_publicationB
            rel_type = self.relation_type.name
        elif self.related_publicationB == entity:
            rel_publication = self.related_publicationA
            rel_type = self.relation_type.name_reverse
        result = {
            'relation_pk': self.pk,
            'relation_type': rel_type,
            'related_place': rel_publication,
            'start_date': self.start_date,
            'end_date': self.end_date}
        return result


    
    
    
    
    