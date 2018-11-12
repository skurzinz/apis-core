import lxml.etree as ET

from django.utils.text import slugify

from . partials import TEI_NSMAP, tei_gen_header


class TeiEntCreator():
    def __init__(self, ent_dict):
        self.nsmap = TEI_NSMAP
        self.project = "APIS"
        self.base_url = "/apis/api2/entity/"
        self.ent_dict = ent_dict
        self.ent_name = ent_dict.get('name', 'No name provided')
        self.ent_type = ent_dict.get('entity_type')
        self.ent_apis_id = ent_dict.get('id')
        self.gen_tei_header = tei_gen_header

    def relation_groups(self):
        ent_dict = self.ent_dict
        ent_types = list(ent_dict['relations'].keys())
        self_type = "{}s".format(ent_dict['entity_type'].lower())
        relations = []
        for x in ent_types:
            group = []
            for y in ent_dict['relations'][x]:
                ent_key = list(y.keys())[2]
                rel = {}
                rel['rel_type'] = x
                rel['rel_label'] = slugify(y['relation_label'])
                rel['target'] = y[ent_key]['id']
                rel['target_name'] = y[ent_key]['name']
                group.append(rel)
            if group:
                relations.append(group)
        return relations

    def relation_notes(self):
        notes = []
        for group in self.relation_groups():
            note = ET.Element("{http://www.tei-c.org/ns/1.0}note")
            note_type = group[0]['rel_type']
            note.attrib['type'] = note_type
            for item in group:
                ptr = ET.Element("ptr")
                ptr.attrib['type'] = item['rel_label']
                ptr.attrib['target'] = "{}{}".format(self.base_url, item['target'])
                note.append(ptr)
            notes.append(note)
        return notes

    def uris_to_idnos(self):
        uris = []
        if self.ent_dict.get('uris'):
            for x in self.ent_dict.get('uris'):
                idno = ET.Element("idno")
                idno.attrib['type'] = 'URL'
                if "d-nb.info" in x.get('uri'):
                    idno.attrib['subtype'] = "GND"
                idno.text = x.get('uri')
                uris.append(idno)
        return uris

    def create_work_node(self):
        work = ET.Element("{http://www.tei-c.org/ns/1.0}item")
        work.attrib['{http://www.w3.org/XML/1998/namespace}id'] = "work__{}".format(
            self.ent_apis_id
        )
        work.text = self.ent_dict.get('name')
        for x in self.relation_notes():
            work.append(x)

        return work

    def create_event_node(self):
        event = ET.Element("{http://www.tei-c.org/ns/1.0}event")
        event.attrib['{http://www.w3.org/XML/1998/namespace}id'] = "event__{}".format(
            self.ent_apis_id
        )
        if self.ent_dict.get('start_date'):
            event.attrib['notBefore'] = self.ent_dict.get('start_date')
        if self.ent_dict.get('end_date'):
            event.attrib['notAfter'] = self.ent_dict.get('end_date')
        for x in self.relation_notes():
            event.append(x)
        label = ET.Element("label")
        label.text = self.ent_dict.get('name')
        event.append(label)
        if self.ent_dict.get('uris'):
            for x in self.ent_dict.get('uris'):
                event.attrib['ref'] = x.get('uri')
        return event

    def create_org_node(self):
        org = ET.Element("{http://www.tei-c.org/ns/1.0}org")
        org.attrib['{http://www.w3.org/XML/1998/namespace}id'] = "org__{}".format(
            self.ent_apis_id
        )
        orgName = ET.Element("orgName")
        orgName.text = self.ent_dict.get('name')
        if self.ent_dict.get('start_date'):
            orgName.attrib['notBefore'] = self.ent_dict.get('start_date')
        if self.ent_dict.get('end_date'):
            orgName.attrib['notAfter'] = self.ent_dict.get('end_date')
        org.append(orgName)
        for x in self.relation_notes():
            org.append(x)
        if self.uris_to_idnos():
            for x in self.uris_to_idnos():
                org.append(x)
        return org

    def create_place_node(self):
        place = ET.Element("{http://www.tei-c.org/ns/1.0}place")
        place.attrib['{http://www.w3.org/XML/1998/namespace}id'] = "place__{}".format(
            self.ent_apis_id
        )
        placeName = ET.Element("placeName")
        placeName.text = self.ent_dict.get('name')
        if self.ent_dict.get('start_date'):
            placeName.attrib['notBefore'] = self.ent_dict.get('start_date')
        if self.ent_dict.get('end_date'):
            placeName.attrib['notAfter'] = self.ent_dict.get('end_date')
        place.append(placeName)
        for x in self.relation_notes():
            place.append(x)
        if self.uris_to_idnos():
            for x in self.uris_to_idnos():
                place.append(x)
        if self.ent_dict.get('lat'):
            coords = "{} {}".format(self.ent_dict['lat'], self.ent_dict['lng'])
            location = ET.Element('location')
            geo = ET.Element('geo')
            geo.text = coords
            location.append(geo)
            place.append(location)
        return place

    def create_person_node(self):
        person = ET.Element("{http://www.tei-c.org/ns/1.0}person")
        person.attrib['{http://www.w3.org/XML/1998/namespace}id'] = "person__{}".format(
            self.ent_apis_id
        )
        persName = ET.Element("persName")
        surname = ET.Element("surname")
        surname.text = self.ent_dict.get('name')
        persName.append(surname)
        if self.ent_dict.get('first_name'):
            forename = ET.Element("forename")
            forename.text = self.ent_dict.get('first_name')
            persName.append(forename)
        person.append(persName)
        if self.ent_dict.get('start_date'):
            birth = ET.Element("birth")
            birth.attrib['when'] = self.ent_dict.get('start_date')
            birth.text = self.ent_dict.get('start_date_written')
            person.append(birth)
        if self.ent_dict.get('end_date'):
            death = ET.Element("death")
            death.attrib['when'] = self.ent_dict.get('end_date')
            death.text = self.ent_dict.get('end_date_written')
            person.append(death)
        for x in self.relation_notes():
            person.append(x)
        if self.uris_to_idnos():
            for x in self.uris_to_idnos():
                person.append(x)
        return person

    def populate_header(self):
        main = "{}: {}".format(self.ent_type, self.ent_name)
        header = self.gen_tei_header.format(main, self.project)
        return header

    def create_header_node(self):
        header = ET.fromstring(self.populate_header())
        return header

    def create_full_doc(self):
        doc = self.create_header_node()
        if self.ent_type == "Person":
            item = self.create_person_node()
            ent_list = ET.Element("listPerson")
        elif self.ent_type == "Place":
            item = self.create_place_node()
            ent_list = ET.Element("listPlace")
        elif self.ent_type == "Institution":
            item = self.create_org_node()
            ent_list = ET.Element("listOrg")
        elif self.ent_type == "Event":
            item = self.create_event_node()
            ent_list = ET.Element("listEvent")
        elif self.ent_type == "Work":
            item = self.create_work_node()
            ent_list = ET.Element("list")
        body = doc.xpath("//tei:body", namespaces=self.nsmap)[0]
        body.append(ent_list)
        ent_list.append(item)
        return doc

    def serialize_full_doc(self):
        return ET.tostring(self.create_full_doc(), pretty_print=True, encoding='UTF-8')

    def export_full_doc(self):
        file = "temp.xml"
        with open(file, 'wb') as f:
            f.write(ET.tostring(self.create_full_doc(), pretty_print=True, encoding='UTF-8'))
        return file
