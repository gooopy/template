def make_ddl(ddls):
    with open('ddl/newDataDefinition.xml', 'w') as f:
        f.write("<?xml version=\"1.0\" encoding=\"EUC-KR\" standalone=\"no\"?>\n")
        f.write("<!DOCTYPE ddl-list SYSTEM \"DataDefinition.dtd\">\n")
        f.write("<ddl-list>\n")
        f.write("\n")
        for ddl in ddls:
        	f.write("<ddl id=\"" + str(ddl.id) + "\">" + "\n")
        	f.write("<title>" + ddl.title + "</title>" + "\n")
        	f.write("<owner>dblab</owner>" + "\n")
        	f.write("creation-date>" + ddl.creation_date.strftime("%s") + "</creation-date>" + "\n")
        	f.write("<comments/>" + "\n")
        	f.write("<attribute-format type=\"variable\">" + "\n")
        	f.write("<field-delimeter>" + ddl.field_delimeter + "</field-delimeter>" + "\n")
        	f.write("<record-delimeter>" + ddl.record_delimeter + "</record-delimeter>" + "\n")
        	f.write("<itemset is-itemset-data=\"false\" itemset-delimeter=\"\">" + "\n")
        	f.write("<tid-index>0</tid-index>" + "\n")
        	f.write("</itemset>" + "\n")
        	f.write("</attribute-format>" + "\n")
        	f.write("<attribute-list>" + "\n")

        	i = 1
        	for attr in ddl.attributes:
        		if len(attr.name) == 0:
        			continue
        		f.write("<attribute id=\"" + str(i) + "\">" + "\n")
        		f.write("<name>" + attr.name + "</name>" + "\n")
        		f.write("<type>" + attr.attr_type + "</type>" + "\n")
        		f.write("<allow-null>")
        		if attr.nullable is True:
        			f.write("true")
        		else:
        			f.write("false")
        		f.write("</allow-null>" + "\n")
        		f.write("<default-value/>" + "\n")
        		f.write("</attribute>" + "\n")
        		i += 1
        	
        	f.write("</attribute-list>" + "\n")
        	f.write("</ddl>" + "\n\n")
        f.write("</ddl-list>" + "\n\n")
