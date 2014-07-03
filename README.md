ANALYSIS OF ENTITIES ON WIKIPEDIA INFOBOXES
=========================================================================
This is done as an assignment for the course Web Mining at IIIT Hyderabad

The format of each <entity-type>.txt is as follows.
There is one line per attribute. Each line contains the following fields separated by a tab.
1. Attribute name
2. Inferred data type of the attribute 
3. If the attribute is numeric, put in the min value observed for that attribute, else put -1
4. If the attribute is numeric, put in the max value observed for that attribute, else put -1
5. units used for the attribute.

*****Methology in brief*****

From the Wikipedia dump, at first we find the <page> tags to identify the different pages.  Then we create separate files for each of the pages.
We feed these pages as input to WikiXMLJ Parser in order to extract and index the portion within the <Infobox> tags from each of the pages. Now, we have the Infoboxes from each of the Wikipedia pages in separate files.
Next we parse the Infobox pages to extract the different desirables.
For each Infobox page:-
1. We first infer the entity type
2. We extract the attribute names by splitting it on the basis of "|". We normalize the attribute names obtained into a uniform state.
3. Similarly the attribute values are extracted.
4. The data types of the attributes are infered.
5. If an attribute is not of type "date" and if it is an alphanumeric value, we separate the alphabet and the numeric parts and conclude that the alphabet portion is the unit of that attribute.
6. We create a table using sqlite for each of the entity types and insert into them rows where each rows contains the attribute name, its data type, its minimum and maximum values and the associated units. The attribute name is the primary key which ensures that unique attribute names. We update the minimum and maximum values at each step as we read new infoboxes.


*****Heuristics used to infer the entity type from the Info boxes*****

We parse the Infobox pages in order to infer the entity type. We split each of the Infobox pages by the new line character. We then take the first portion obtained aftre the split and again split it by the word "Infobox" and take the portion following this word as the entity type of that Infobox.



*****Heuristics used to infer the data type of the attributes*****

If the attribute name contains the substring "date" or if the values contains any of the 12 month names or any of the days in the week, we conclude it is of datatype "date". Otherwise if the attribute value is enclosed within double square brackets or it contains the word "www", we conclude it is of datatype "linlOtherwise, if the value of an attribute is a pure number, we infer that it is of data type 'number'. Otherwise a value contains numbers separated by special characters like colon, hyphen etc, we conclude that it is of type "duration". If a value contains numbers separated by special characters like colon, hyphen etc, which are again separated by special characters like comma, front slash we conclude that it is of type "Set of durations". Otherwise if the value of the attribute contains special characters like comma, front slash, we conclude it is a "Set of Strings". 


*****Average number of attributes per entity type*****

We store the number of attributes for each occurance of each of the entity types in the Wikidump. Then we take the average of that for each of the entity types. This is stored in the file AverageNoOfAttributes.txt

*****Number of entities per entity type*****

While extracting the entity type of each of the Infoboxes, we keep a count of occurances of each entity type in the Wikidump. This is stored in the file NoOfEntitiesForEachEntity.txt
