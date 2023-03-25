# Step to start the project
1. Run- pip install requiremnets.text
2. Create the scheme in you local by the following name -- language_trans_data_creation
3. Now run the following scripts to create the master data in the language table
SQL SCRIPTS :-  
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('1', 'Bengali(bn)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('2', 'Gujrati(gu)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('3', 'Hindi(hi)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('4', 'Kannada(kn)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('5', 'Malayalam(ml)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('6', 'Marathi(mr)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('7', 'Nepali(ne)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('8', 'Oriya(or)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('9', 'Panjabi(pa)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('10', 'Sinhala(si)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('11', 'Tamil(ta)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('12', 'Telgu(te)');
              INSERT INTO `language_trans_data_creation`.`language` (`lang_id`, `language`) VALUES ('13', 'Urdu(ur)');
          
4. Go to the app folder of the project through cmd and run the following command - uvicorn app:app --reload --port 8003
