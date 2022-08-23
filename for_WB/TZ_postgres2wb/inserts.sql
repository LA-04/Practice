#"author" 

INSERT INTO author VALUES ('maks', '/home/maks', '/WorkDir/Subjects', '/WorkDir/Subjects.xlsx', '/WorkDir/Templates', '/WorkDir/Templates.xlsx') ;
INSERT INTO author VALUES ('barbara', '/home/barbara', '/WorkDir/Subjects', '/WorkDir/Subjects.xlsx', '/WorkDir/Templates', '/WorkDir/Templates.xlsx') ;
INSERT INTO author VALUES ('alla', '/home/alla', '/WorkDir/Subjects', '/WorkDir/Subjects.xlsx', '/WorkDir/Templates', '/WorkDir/Templates.xlsx') ;
INSERT INTO author VALUES ('anna', '/home/anna', '/WorkDir/Subjects', '/WorkDir/Subjects.xlsx', '/WorkDir/Templates', '/WorkDir/Templates.xlsx') ;
#SELECT * FROM author ;

# "image_position" 

#INSERT INTO image_position (name) VALUES ('testimgpos') ;
INSERT INTO image_position (name) VALUES ('center') ;
INSERT INTO image_position (name) VALUES ('up') ;
INSERT INTO image_position (name) VALUES ('leftup') ;
INSERT INTO image_position (name) VALUES ('rightup') ;
#SELECT * FROM image_position ;

# "brand" 

INSERT INTO brand (name) VALUES ('none') ;
INSERT INTO brand (name) VALUES ('black') ;
INSERT INTO brand (name) VALUES ('white') ;
#SELECT * FROM brand ;

# "print_zone" }

INSERT INTO print_zone (name, width_px, height_px) VALUES ('notepad_default', 1795, 2528) ;
INSERT INTO print_zone VALUES ('tshirtman_default', 3508, 4961) ;
INSERT INTO print_zone VALUES ('tshirtwoman_default', 3508, 4961) ;
INSERT INTO print_zone VALUES ('cup_default', 2400, 1000) ;
#SELECT * FROM print_zone ;

# "infographic_color" 

INSERT INTO infographic_color (name) VALUES ('black') ;
INSERT INTO infographic_color (name) VALUES ('white') ;
#SELECT * FROM infographic_color ;


# "product_type" 

INSERT INTO product_type VALUES ('notepad_sketch', 'notepad', 'sketch', 'notepad_default', '/notepad') ;
INSERT INTO product_type VALUES ('notepad_clear', 'notepad', 'clear', 'notepad_default', '/notepad') ;
INSERT INTO product_type VALUES ('notepad_line', 'notepad', 'line', 'notepad_default', '/notepad') ;
INSERT INTO product_type VALUES ('notepad_point', 'notepad', 'point', 'notepad_default', '/notepad') ;
INSERT INTO product_type VALUES ('notepad_square', 'notepad', 'square', 'notepad_default', '/notepad') ;

#SELECT * FROM product_type ;


INSERT INTO product_type VALUES ('tshirtblack_man', 'tshirtblack', 'man', 'tshirtman_default', '/tshirtblack/man') ;
INSERT INTO product_type VALUES ('tshirtwhite_man', 'tshirtwhite', 'man', 'tshirtman_default', '/tshirtwhite/man') ;
INSERT INTO product_type VALUES ('tshirtblack_woman', 'tshirtblack', 'woman', 'tshirtwoman_default', '/tshirtblack/woman') ;
INSERT INTO product_type VALUES ('tshirtwhite_woman', 'tshirtwhite', 'woman', 'tshirtwoman_default', '/tshirtwhite/woman') ;
#SELECT * FROM product_type ;

INSERT INTO product_type VALUES ('cup_white', 'cup', 'white', 'cup_default', '/cup/white') ;

#SELECT * FROM product_type ;

# "common_photo" 

INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'notepad_sketch', '/common/notepad/sketch') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'notepad_clear', '/common/notepad/clear') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'notepad_line', '/common/notepad/line') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'notepad_point', '/common/notepad/point') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'notepad_square', '/common/notepad/square') ;

INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'tshirtwhite_man', '/common/tshirtwhite/man') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'tshirtblack_man', '/common/tshirtblack/man') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'tshirtwhite_woman', '/common/tshirtwoman/woman') ;
INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'tshirtblack_woman', '/common/tshirblack/woman') ;

INSERT INTO common_photo (name, product_type, path_dir) VALUES ('default', 'cup_white', '/common/cup/white') ;

#SELECT * FROM common_photo ;

# "template_group" 

INSERT INTO template_group VALUES ('testtemplgroup', '/groups/testtemplgroup.png') ;
#SELECT * FROM template_group ;

# "template" 

INSERT INTO template VALUES ('testtempl', 'testtemplgroup', 'maks', '/templates/testtempl.xlsx', '/templates/testtempl.json') ;
#SELECT * FROM template ;

# "subject" 

INSERT INTO subject VALUES ('testsubj', 3, 'testtempl', 'anna', '/subjects/testsubj') ;
#SELECT * from subject ;

# "mockup" 

INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'notepad_sketch',
	'/mockups/notepad_default_1.xcf',
	'(),(),(),()',
	'/mockups/notepad_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'notepad_clear',
	'/mockups/notepad_default_1.xcf',
	'(),(),(),()',
	'/mockups/notepad_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'notepad_point',
	'/mockups/notepad_default_1.xcf',
	'(),(),(),()',
	'/mockups/notepad_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'notepad_line',
	'/mockups/notepad_default_1.xcf',
	'(),(),(),()',
	'/mockups/notepad_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'notepad_square',
	'/mockups/notepad_default_1.xcf',
	'(),(),(),()',
	'/mockups/notepad_default_2.xcf',
	'(),(),(),()'
);

#SELECT * FROM mockup ;

INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'tshirtwhite_man',
	'/mockups/tshirtwhite_man_default_1.xcf',
	'(),(),(),()',
	'/mockups/tshirtwhite_man_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'tshirtblack_man',
	'/mockups/tshirtblack_man_default_1.xcf',
	'(),(),(),()',
	'/mockups/tshirtblack_man_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'tshirtwhite_woman',
	'/mockups/tshirtwhite_woman_default_1.xcf',
	'(),(),(),()',
	'/mockups/tshirtwhite_woman_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'tshirtblack_woman',
	'/mockups/tshirtblack_woman_default_1.xcf',
	'(),(),(),()',
	'/mockups/tshirtblack_woman_default_2.xcf',
	'(),(),(),()'
);
INSERT INTO mockup (name, product_type, path_mockup1, params1, path_mockup2, params2) VALUES (
	'default',
	'cup_white',
	'/mockups/cup_white_default_1.xcf',
	'(),(),(),()',
	'/mockups/cup_white_default_2.xcf',
	'(),(),(),()'
);

#SELECT * FROM mockup ;

# "infographic" 

INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_sketch',
	'default',
	'black',
	'/infographics/notepad/sketch/black/0.png',
	'/infographics/notepad/sketch/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_clear',
	'default',
	'black',
	'/infographics/notepad/clear/black/0.png',
	'/infographics/notepad/clear/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_point',
	'default',
	'black',
	'/infographics/notepad/point/black/0.png',
	'/infographics/notepad/point/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_square',
	'default',
	'black',
	'/infographics/notepad/square/black/0.png',
	'/infographics/notepad/square/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_line',
	'default',
	'black',
	'/infographics/notepad/line/black/0.png',
	'/infographics/notepad/line/black/1.png'
);

INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_sketch',
	'default',
	'white',
	'/infographics/notepad/sketch/white/0.png',
	'/infographics/notepad/sketch/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_clear',
	'default',
	'white',
	'/infographics/notepad/clear/white/0.png',
	'/infographics/notepad/clear/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_point',
	'default',
	'white',
	'/infographics/notepad/point/white/0.png',
	'/infographics/notepad/point/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_square',
	'default',
	'white',
	'/infographics/notepad/square/white/0.png',
	'/infographics/notepad/square/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'notepad_line',
	'default',
	'white',
	'/infographics/notepad/line/white/0.png',
	'/infographics/notepad/line/white/1.png'
);

#SELECT * FROM infographic ;

INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtwhite_man',
	'default',
	'black',
	'/infographics/tshirtwhite/man/black/0.png',
	'/infographics/tshirtwhite/man/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtwhite_woman',
	'default',
	'black',
	'/infographics/tshirtwhite/woman/black/0.png',
	'/infographics/tshirtwhite/woman/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtblack_man',
	'default',
	'black',
	'/infographics/tshirtblack/man/black/0.png',
	'/infographics/tshirtblack/man/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtblack_woman',
	'default',
	'black',
	'/infographics/tshirtblack/woman/black/0.png',
	'/infographics/tshirtblack/woman/black/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'cup_white',
	'default',
	'black',
	'/infographics/cup/white/black/0.png',
	'/infographics/cup/white/black/1.png'
);


INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtwhite_man',
	'default',
	'white',
	'/infographics/tshirtwhite/man/white/0.png',
	'/infographics/tshirtwhite/man/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtwhite_woman',
	'default',
	'white',
	'/infographics/tshirtwhite/woman/white/0.png',
	'/infographics/tshirtwhite/woman/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtblack_man',
	'default',
	'white',
	'/infographics/tshirtblack/man/white/0.png',
	'/infographics/tshirtblack/man/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'tshirtblack_woman',
	'default',
	'white',
	'/infographics/tshirtblack/woman/white/0.png',
	'/infographics/tshirtblack/woman/white/1.png'
);
INSERT INTO infographic (name, product_type, mockup, color, path_infogr1, path_infogr2) VALUES(
	'default',
	'cup_white',
	'default',
	'white',
	'/infographics/cup/white/white/0.png',
	'/infographics/cup/white/white/1.png'
);


# "product_group" 

INSERT INTO product_group VALUES (
	'testsubj_notepad_sketch',
	'testsubj',
	'notepad_sketch',
	'default',
	'default',
	'default',
	'black',
	100,
	'none',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/notepad'
);
INSERT INTO product_group VALUES (
	'testsubj_notepad_line',
	'testsubj',
	'notepad_line',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/notepad'
);

INSERT INTO product_group VALUES (
	'testsubj_notepad_point',
	'testsubj',
	'notepad_point',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/notepad'
);

INSERT INTO product_group VALUES (
	'testsubj_notepad_clear',
	'testsubj',
	'notepad_clear',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/notepad'
);

INSERT INTO product_group VALUES (
	'testsubj_notepad_square',
	'testsubj',
	'notepad_square',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/notepad'
);

INSERT INTO product_group VALUES (
	'testsubj_tshirtblack_man',
	'testsubj',
	'tshirtblack_man',
	'default',
	'default',
	'default',
	'white',
	100,
	'white',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/tshirtblack/man'
);

INSERT INTO product_group VALUES (
	'testsubj_tshirtwhite_man',
	'testsubj',
	'tshirtwhite_man',
	'default',
	'default',
	'default',
	'white',
	100,
	'white',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/tshirtwhite/man'
);


INSERT INTO product_group VALUES (
	'testsubj_tshirtwhite_woman',
	'testsubj',
	'tshirtwhite_woman',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(190 120 180)',
	'/subjects/testsubj/tshirtwhite/woman'
);

INSERT INTO product_group VALUES (
	'testsubj_tshirtblack_woman',
	'testsubj',
	'tshirtblack_woman',
	'default',
	'default',
	'default',
	'black',
	80,
	'black',
	'center',
	'#(19 109 204)',
	'#(190 120 180)',
	'/subjects/testsubj/tshirblack/woman'
);

INSERT INTO product_group VALUES (
	'testsubj_cup_white',
	'testsubj',
	'cup_white',
	'default',
	'default',
	'default',
	'black',
	80,
	'white',
	'center',
	'#(19 109 204)',
	'#(89 120 180)',
	'/subjects/testsubj/cup/white'
);

#SELECT * FROM product_group ;

# "product" 

#notepad_sketch

INSERT INTO product VALUES (
	'testsubj_notepad_sketch-0', 
	'testsubj_notepad_sketch', 
	0,
	0,
	'/subjects/testsubj/notepad/mockups/item_0',
	'/subjects/testsubj/notepad/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_sketch-1', 
	'testsubj_notepad_sketch', 
	1,
	0,
	'/subjects/testsubj/notepad/mockups/item_1',
	'/subjects/testsubj/notepad/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_sketch-2', 
	'testsubj_notepad_sketch', 
	2,
	0,
	'/subjects/testsubj/notepad/mockups/item_2',
	'/subjects/testsubj/notepad/prints/2.png'
);

#notepad_line

INSERT INTO product VALUES (
	'testsubj_notepad_line-0', 
	'testsubj_notepad_line', 
	0,
	0,
	'/subjects/testsubj/notepad/mockups/item_0',
	'/subjects/testsubj/notepad/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_line-1', 
	'testsubj_notepad_line', 
	1,
	0,
	'/subjects/testsubj/notepad/mockups/item_1',
	'/subjects/testsubj/notepad/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_line-2', 
	'testsubj_notepad_line', 
	2,
	0,
	'/subjects/testsubj/notepad/mockups/item_2',
	'/subjects/testsubj/notepad/prints/2.png'
);

#notepad_point

INSERT INTO product VALUES (
	'testsubj_notepad_point-0', 
	'testsubj_notepad_point', 
	0,
	0,
	'/subjects/testsubj/notepad/mockups/item_0',
	'/subjects/testsubj/notepad/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_point-1', 
	'testsubj_notepad_point', 
	1,
	0,
	'/subjects/testsubj/notepad/mockups/item_1',
	'/subjects/testsubj/notepad/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_point-2', 
	'testsubj_notepad_point', 
	2,
	0,
	'/subjects/testsubj/notepad/mockups/item_2',
	'/subjects/testsubj/notepad/prints/2.png'
);

#notepad_clear

INSERT INTO product VALUES (
	'testsubj_notepad_clear-0', 
	'testsubj_notepad_clear', 
	0,
	0,
	'/subjects/testsubj/notepad/mockups/item_0',
	'/subjects/testsubj/notepad/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_clear-1', 
	'testsubj_notepad_clear', 
	1,
	0,
	'/subjects/testsubj/notepad/mockups/item_1',
	'/subjects/testsubj/notepad/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_clear-2', 
	'testsubj_notepad_clear', 
	2,
	0,
	'/subjects/testsubj/notepad/mockups/item_2',
	'/subjects/testsubj/notepad/prints/2.png'
);

#notepad_square

INSERT INTO product VALUES (
	'testsubj_notepad_square-0', 
	'testsubj_notepad_square', 
	0,
	0,
	'/subjects/testsubj/notepad/mockups/item_0',
	'/subjects/testsubj/notepad/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_square-1', 
	'testsubj_notepad_square', 
	1,
	0,
	'/subjects/testsubj/notepad/mockups/item_1',
	'/subjects/testsubj/notepad/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_notepad_square-2', 
	'testsubj_notepad_square', 
	2,
	0,
	'/subjects/testsubj/notepad/mockups/item_2',
	'/subjects/testsubj/notepad/prints/2.png'
);

#tshirtblack_man

INSERT INTO product VALUES (
	'testsubj_tshirtblack_man-0', 
	'testsubj_tshirtblack_man', 
	0,
	0,
	'/subjects/testsubj/tshirtblack/man/mockups/item_0',
	'/subjects/testsubj/tshirtblack/man/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtblack_man-1', 
	'testsubj_tshirtblack_man', 
	1,
	0,
	'/subjects/testsubj/tshirtblack/man/mockups/item_1',
	'/subjects/testsubj/tshirtblack/man/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtblack_man-2', 
	'testsubj_tshirtblack_man', 
	2,
	0,
	'/subjects/testsubj/tshirtblack/man/mockups/item_2',
	'/subjects/testsubj/tshirtblack/man/prints/2.png'
);

#tshirtwhite_man

INSERT INTO product VALUES (
	'testsubj_tshirtwhite_man-0', 
	'testsubj_tshirtwhite_man', 
	0,
	0,
	'/subjects/testsubj/tshirtwhite/man/mockups/item_0',
	'/subjects/testsubj/tshirtwhite/man/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtwhite_man-1', 
	'testsubj_tshirtwhite_man', 
	1,
	0,
	'/subjects/testsubj/tshirtwhite/man/mockups/item_1',
	'/subjects/testsubj/tshirtwhite/man/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtwhite_man-2', 
	'testsubj_tshirtwhite_man', 
	2,
	0,
	'/subjects/testsubj/tshirtwhite/man/mockups/item_2',
	'/subjects/testsubj/tshirtwhite/man/prints/2.png'
);

#tshirtwhite_woman

INSERT INTO product VALUES (
	'testsubj_tshirtwhite_woman-0', 
	'testsubj_tshirtwhite_woman', 
	0,
	0,
	'/subjects/testsubj/tshirtwhite/woman/mockups/item_0',
	'/subjects/testsubj/tshirtwhite/woman/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtwhite_woman-1', 
	'testsubj_tshirtwhite_woman', 
	1,
	0,
	'/subjects/testsubj/tshirtwhite/woman/mockups/item_1',
	'/subjects/testsubj/tshirtwhite/woman/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtwhite_woman-2', 
	'testsubj_tshirtwhite_woman', 
	2,
	0,
	'/subjects/testsubj/tshirtwhite/woman/mockups/item_2',
	'/subjects/testsubj/tshirtwhite/woman/prints/2.png'
);

#tshirtblack_woman

INSERT INTO product VALUES (
	'testsubj_tshirtblack_woman-0', 
	'testsubj_tshirtblack_woman', 
	0,
	0,
	'/subjects/testsubj/tshirtblack/woman/mockups/item_0',
	'/subjects/testsubj/tshirtblack/woman/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtblack_woman-1', 
	'testsubj_tshirtblack_woman', 
	1,
	0,
	'/subjects/testsubj/tshirtblack/woman/mockups/item_1',
	'/subjects/testsubj/tshirtblack/woman/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_tshirtblack_woman-2', 
	'testsubj_tshirtblack_woman', 
	2,
	0,
	'/subjects/testsubj/tshirtblack/woman/mockups/item_2',
	'/subjects/testsubj/tshirtblack/woman/prints/2.png'
);

#cup_white

INSERT INTO product VALUES (
	'testsubj_cup_white-0', 
	'testsubj_cup_white', 
	0,
	0,
	'/subjects/testsubj/cup/white/mockups/item_0',
	'/subjects/testsubj/cup/white/prints/0.png'
);
INSERT INTO product VALUES (
	'testsubj_cup_white-1', 
	'testsubj_cup_white', 
	1,
	0,
	'/subjects/testsubj/cup/white/mockups/item_1',
	'/subjects/testsubj/cup/white/prints/1.png'
);
INSERT INTO product VALUES (
	'testsubj_cup_white-2', 
	'testsubj_cup_white', 
	2,
	0,
	'/subjects/testsubj/cup/white/mockups/item_2',
	'/subjects/testsubj/cup/white/prints/2.png'
);

#SELECT * FROM product ;

#"upload_list"

INSERT INTO upload_list (product) VALUES ('testsubj_notepad_sketch-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_sketch-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_sketch-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_line-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_line-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_line-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_point-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_point-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_point-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_clear-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_clear-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_clear-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_square-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_square-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_notepad_square-2') ;

INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_man-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_man-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_man-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_man-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_man-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_man-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_woman-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_woman-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtwhite_woman-2') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_woman-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_woman-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_tshirtblack_woman-2') ;

INSERT INTO upload_list (product) VALUES ('testsubj_cup_white-0') ;
INSERT INTO upload_list (product) VALUES ('testsubj_cup_white-1') ;
INSERT INTO upload_list (product) VALUES ('testsubj_cup_white-2') ;


#"wb_vase_card"

INSERT INTO wb_base_card VALUES (
	'notepad_sketch',
	'base_notepad_sketch-0',
	'2032939644626',
	576,
	22,
	900,
	'/base_cards/base_notepad_sketch.json',
	'/insert_fields/insert_notepad_sketch.json'
);

INSERT INTO wb_base_card VALUES (
	'notepad_clear',
	'base_notepad_clear-0',
	'2032937124625',
	436,
	20,
	900,
	'/base_cards/base_notepad_clear.json',
	'/insert_fields/insert_notepad_clear.json'
);

INSERT INTO wb_base_card VALUES (
	'notepad_point',
	'base_notepad_point-0',
	'2032942151623',
	436,
	20,
	900,
	'/base_cards/base_notepad_point.json',
	'/insert_fields/insert_notepad_point.json'
);

INSERT INTO wb_base_card VALUES (
	'notepad_square',
	'base_notepad_square-0',
	'2032940815626',
	436,
	20,
	900,
	'/base_cards/base_notepad_square.json',
	'/insert_fields/insert_notepad_square.json'
);

INSERT INTO wb_base_card VALUES (
	'notepad_line',
	'base_notepad_line-0',
	'2032944800628',
	436,
	20,
	900,
	'/base_cards/base_notepad_line.json',
	'/insert_fields/insert_notepad_line.json'
);

INSERT INTO wb_base_card VALUES (
	'tshirtblack_man',
	'base_tshirtblack_man-0',
	'2032933899633',
	1200,
	20,
	100,
	'/base_cards/base_tshirtblack_man.json',
	'/insert_fields/insert_tshirtblack_man.json'
);

INSERT INTO wb_base_card VALUES (
	'tshirtblack_woman',
	'base_tshirtblack_woman-0',
	'2032932357646',
	1200,
	20,
	100,
	'/base_cards/base_tshirtblack_woman.json',
	'/insert_fields/insert_tshirtblack_woman.json'
);

INSERT INTO wb_base_card VALUES (
	'tshirtwhite_man',
	'base_tshirtwhite_man-0',
	'2032935798644',
	1200,
	20,
	100,
	'/base_cards/base_tshirtwhite_man.json',
	'/insert_fields/insert_tshirtwhite_man.json'
);

INSERT INTO wb_base_card VALUES (
	'tshirtwhite_woman',
	'base_tshirtwhite_woman-0',
	'2032929592623',
	1200,
	20,
	100,
	'/base_cards/base_tshirtwhite_woman.json',
	'/insert_fields/insert_tshirtwhite_woman.json'
);

INSERT INTO wb_base_card VALUES (
	'cup_white',
	'base_cup_white-0',
	'2032926791623',
	550,
	20,
	900,
	'/base_cards/base_cup_white.json',
	'/insert_fields/insert_cup_white.json'
);



