stock_numbers_list = ['500002', '500003', '500008', '500010', '500012', '500013', '500020', '500023', '500027', '500031', '500032', '500033', '500034', '500038', '500039', '500040', '500041', '500042', '500043', '500048', '500049', '500052', '500060', '500067', '500074', '500078', '500083', '500084', '500085', '500086', '500087', '500089', '500093', '500096', '500097', '500101', '500103', '500104', '500106', '500108', '500109', '500110', '500111', '500112', '500113', '500114', '500116', '500117', '500119', '500123', '500124', '500125', '500126', '500128', '500133', '500135', '500136', '500144', '500148', '500150', '500151', '500153', '500160', '500163', '500164', '500165', '500168', '500171', '500173', '500179', '500180', '500182', '500183', '500184', '500185', '500186', '500187', '500188', '500189', '500193', '500199', '500201', '500207', '500209', '500210', '500214', '500215', '500219', '500227', '500228', '500231', '500233', '500234', '500235', '500238', '500241', '500243', '500245', '500247', '500249', '500250', '500251', '500252', '500253', '500257', '500259', '500260', '500265', '500266', '500268', '500271', '500279', '500280', '500285', '500288', '500290', '500292', '500294', '500295', '500296', '500298', '500300', '500304', '500307', '500312', '500313', '500314', '500317', '500325', '500327', '500330', '500331', '500335', '500336', '500338', '500339', '500343', '500346', '500350', '500354', '500355', '500356', '500366', '500368', '500378', '500380', '500387', '500390', '500400', '500402', '500403', '500404', '500405', '500407', '500408', '500410', '500411', '500412', '500413', '500418', '500420', '500425', '500429', '500439', '500440', '500444', '500449', '500456', '500459', '500460', '500463', '500464', '500467', '500469', '500470', '500472', '500477', '500480', '500483', '500488', '500490', '500493', '500495', '500500', '500510', '500520', '500530', '500540', '500547', '500550', '500570', '500575', '500620', '500645', '500650', '500655', '500660', '500670', '500672', '500674', '500680', '500690', '500696', '500710', '500730', '500770', '500777', '500780', '500790', '500800', '500820', '500825', '500830', '500840', '500850', '500870', '500875', '500877', '500878', '500890', '500940', '501242', '501295', '501301', '501343', '501423', '501425', '501455', '501831', '502090', '502137', '502157', '502168', '502180', '502219', '502330', '502355', '502420', '502448', '502450', '502742', '502820', '502865', '502937', '502986', '503031', '503100', '503101', '503169', '503310', '503722', '503806', '503811', '503960', '504036', '504058', '504067', '504112', '504212', '504286', '504375', '504614', '504741', '504746', '504879', '504918', '504966', '504973', '504998', '505010', '505075', '505141', '505160', '505192', '505196', '505200', '505242', '505255', '505283', '505324', '505355', '505368', '505400', '505412', '505509', '505533', '505537', '505590', '505688', '505700', '505710', '505714', '505720', '505726', '505744', '505790', '505800', '505807', '505854', '505890', '506022', '506074', '506076', '506109', '506120', '506146', '506184', '506194', '506197', '506222', '506235', '506261', '506285', '506313', '506390', '506395', '506401', '506405', '506480', '506525', '506579', '506590', '506618', '506655', '506685', '506687', '506690', '506767', '506820', '506943', '506945', '506947', '506975', '507205', '507315', '507410', '507438', '507442', '507488', '507490', '507514', '507526', '507543', '507552', '507580', '507663', '507685', '507717', '507747', '507779', '507785', '507789', '507794', '507808', '507815', '507828', '507880', '507938', '507987', '508486', '508814', '508869', '508906', '508933', '508989', '509009', '509020', '509055', '509077', '509079', '509099', '509152', '509220', '509243', '509480', '509488', '509496', '509557', '509567', '509631', '509635', '509675', '509692', '509709', '509715', '509820', '509845', '509874', '509910', '509930', '509966', '511018', '511034', '511108', '511169', '511194', '511196', '511208', '511218', '511243', '511413', '511431', '511505', '511559', '511630', '511634', '511676', '511726', '511742', '511766', '512004', '512011', '512038', '512060', '512063', '512070', '512091', '512131', '512157', '512161', '512179', '512195', '512237', '512245', '512296', '512303', '512337', '512404', '512415', '512433', '512455', '512461', '512519', '512522', '512529', '512531', '512553', '512573', '512591', '512597', '512599', '512608', '512626', '513010', '513023', '513097', '513108', '513121', '513216', '513228', '513262', '513269', '513343', '513349', '513375', '513377', '513434', '513436', '513446', '513496', '513507', '513509', '513517', '513519', '513540', '513554', '513599', '513683', '513729', '514034', '514043', '514045', '514142', '514162', '514167', '514175', '514183', '514211', '514234', '514248', '514274', '514286', '514300', '514318', '514354', '514402', '514418', '514450', '514470', '515030', '515037', '515055', '515093', '515145', '516016', '516022', '516064', '516072', '516082', '516092', '517015', '517041', '517059', '517146', '517168', '517172', '517174', '517206', '517214', '517271', '517273', '517300', '517330', '517334', '517344', '517354', '517360', '517380', '517385', '517421', '517447', '517498', '517506', '517522', '517530', '517536', '517544', '517556', '517562', '517569', '517571', '518029', '518091', '519091', '519105', '519126', '519136', '519156', '519183', '519224', '519307', '519383', '519413', '519415', '519494', '519506', '519552', '519588', '519600', '519602', '520008', '520021', '520043', '520051', '520056', '520057', '520059', '520066', '520081', '520086', '520111', '520113', '520119', '520131', '520151', '521003', '521016', '521018', '521034', '521064', '521068', '521070', '521109', '521133', '521137', '521163', '521180', '521200', '521220', '521232', '521248', '522014', '522029', '522034', '522064', '522073', '522074', '522108', '522113', '522205', '522215', '522217', '522241', '522249', '522263', '522275', '522285', '522287', '522295', '523011', '523025', '523127', '523204', '523207', '523242', '523260', '523261', '523269', '523283', '523301', '523315', '523319', '523323', '523351', '523367', '523369', '523371', '523384', '523385', '523391', '523395', '523398', '523405', '523419', '523445', '523457', '523465', '523539', '523574', '523598', '523610', '523618', '523628', '523630', '523642', '523648', '523660', '523694', '523704', '523708', '523716', '523736', '523754', '523756', '523790', '523792', '523828', '523836', '523838', '524000', '524013', '524019', '524051', '524075', '524091', '524109', '524129', '524164', '524200', '524208', '524212', '524226', '524230', '524280', '524330', '524332', '524348', '524370', '524372', '524394', '524396', '524404', '524412', '524494', '524500', '524502', '524518', '524558', '524570', '524598', '524604', '524652', '524663', '524667', '524669', '524709', '524715', '524735', '524742', '524774', '524804', '524816', '524820', '524824', '526027', '526173', '526217', '526227', '526235', '526247', '526263', '526299', '526325', '526367', '526371', '526381', '526397', '526423', '526488', '526521', '526550', '526576', '526582', '526596', '526608', '526612', '526628', '526642', '526650', '526662', '526666', '526668', '526725', '526729', '526797', '526807', '526829', '526849', '526881', '526885', '526947', '526951', '526953', '526977', '526983', '526987', '527001', '530001', '530005', '530007', '530011', '530017', '530019', '530023', '530073', '530075', '530117', '530131', '530135', '530161', '530199', '530239', '530299', '530307', '530343', '530355', '530363', '530365', '530367', '530377', '530517', '530549', '530555', '530655', '530683', '530705', '530741', '530759', '530803', '530813', '530843', '530871', '530905', '530917', '530919', '530929', '530961', '530965', '530999', '531035', '531082', '531092', '531111', '531120', '531146', '531147', '531162', '531179', '531209', '531213', '531227', '531241', '531266', '531322', '531335', '531344', '531349', '531373', '531381', '531426', '531431', '531439', '531449', '531453', '531497', '531500', '531508', '531518', '531521', '531531', '531543', '531548', '531556', '531595', '531599', '531624', '531628', '531633', '531640', '531642', '531717', '531719', '531735', '531743', '531746', '531761', '531768', '531795', '531847', '531879', '531885', '531921', '531971', '531978', '532019', '532029', '532051', '532054', '532105', '532134', '532141', '532143', '532144', '532149', '532150', '532155', '532156', '532160', '532162', '532163', '532172', '532173', '532174', '532175', '532178', '532180', '532181', '532187', '532189', '532209', '532210', '532212', '532215', '532216', '532218', '532219', '532221', '532234', '532240', '532256', '532259', '532268', '532281', '532286', '532296', '532300', '532301', '532305', '532309', '532310', '532313', '532321', '532324', '532326', '532331', '532335', '532339', '532341', '532343', '532345', '532348', '532349', '532351', '532356', '532357', '532365', '532366', '532368', '532369', '532370', '532371', '532374', '532375', '532376', '532382', '532386', '532387', '532388', '532390', '532392', '532395', '532400', '532408', '532411', '532413', '532419', '532424', '532430', '532432', '532439', '532440', '532443', '532454', '532456', '532457', '532460', '532461', '532466', '532468', '532475', '532477', '532478', '532479', '532481', '532482', '532483', '532485', '532486', '532488', '532493', '532497', '532498', '532500', '532504', '532505', '532507', '532508', '532509', '532513', '532514', '532515', '532521', '532522', '532523', '532524', '532525', '532527', '532528', '532529', '532531', '532532', '532538', '532539', '532540', '532541', '532543', '532548', '532553', '532555', '532604', '532605', '532610', '532612', '532613', '532616', '532621', '532624', '532627', '532628', '532629', '532630', '532633', '532637', '532638', '532640', '532641', '532642', '532644', '532648', '532649', '532650', '532651', '532652', '532654', '532659', '532660', '532661', '532662', '532663', '532666', '532667', '532668', '532670', '532673', '532674', '532676', '532678', '532679', '532683', '532684', '532686', '532687', '532689', '532695', '532698', '532699', '532700', '532702', '532705', '532706', '532707', '532710', '532712', '532713', '532714', '532716', '532717', '532719', '532720', '532721', '532722', '532725', '532726', '532728', '532729', '532730', '532731', '532732', '532733', '532734', '532735', '532740', '532741', '532742', '532748', '532749', '532754', '532755', '532756', '532757', '532759', '532760', '532761', '532762', '532764', '532767', '532768', '532771', '532772', '532773', '532775', '532776', '532777', '532779', '532780', '532782', '532783', '532784', '532785', '532790', '532794', '532795', '532796', '532797', '532798', '532799', '532800', '532801', '532804', '532805', '532807', '532808', '532809', '532810', '532811', '532812', '532814', '532815', '532817', '532819', '532822', '532826', '532827', '532828', '532830', '532832', '532834', '532839', '532842', '532843', '532845', '532847', '532848', '532850', '532851', '532853', '532856', '532859', '532864', '532867', '532868', '532869', '532870', '532872', '532875', '532878', '532880', '532884', '532885', '532886', '532888', '532889', '532890', '532891', '532892', '532894', '532895', '532896', '532898', '532899', '532900', '532902', '532904', '532906', '532916', '532921', '532922', '532923', '532924', '532925', '532926', '532927', '532928', '532929', '532930', '532931', '532932', '532934', '532935', '532937', '532939', '532940', '532941', '532942', '532944', '532945', '532946', '532947', '532951', '532952', '532953', '532955', '532959', '532966', '532967', '532976', '532977', '532978', '532980', '532983', '532986', '532987', '532988', '532989', '532993', '532994', '532998', '533001', '533007', '533012', '533022', '533023', '533029', '533033', '533047', '533080', '533088', '533090', '533093', '533095', '533096', '533098', '533104', '533106', '533121', '533122', '533137', '533138', '533146', '533148', '533150', '533151', '533152', '533155', '533156', '533158', '533160', '533161', '533162', '533163', '533164', '533166', '533168', '533169', '533179', '533181', '533192', '533193', '533203', '533206', '533207', '533208', '533217', '533218', '533227', '533229', '533239', '533248', '533252', '533259', '533260', '533261', '533262', '533263', '533265', '533267', '533269', '533270', '533271', '533272', '533273', '533274', '533275', '533278', '533282', '533284', '533286', '533287', '533292', '533293', '533295', '533296', '533298', '533302', '533303', '533306', '533316', '533317', '533320', '533326', '533329', '533333', '533336', '533339', '533343', '533344', '533393', '533398', '533400', '533451', '533470', '533482', '533519', '533520', '533540', '533543', '533552', '533553', '533573', '533576', '533581', '533605', '533629', '533638', '533644', '533655', '533704', '533758', '533761', '533941', '533982', '534076', '534091', '534109', '534139', '534309', '534312', '534328', '534369', '534392', '534425', '534532', '534563', '534597', '534598', '534600', '534615', '534659', '534674', '534675', '534708', '534742', '534748', '534758', '534809', '534816', '534976', '535276', '535279', '535322', '535458', '535601', '535602', '535647', '535648', '535754', '535755', '535789', '535910', '536456', '536507', '536672', '536710', '536737', '536960', '537007', '537008', '537254', '537259', '537291', '537292', '537326', '537483', '537492', '537573', '537582', '537669', '537708', '537766', '537784', '537785', '537820', '538057', '538119', '538268', '538365', '538402', '538496', '538546', '538562', '538566', '538567', '538576', '538579', '538598', '538635', '538666', '538667', '538668', '538683', '538685', '538706', '538713', '538715', '538730', '538731', '538732', '538733', '538734', '538765', '538794', '538817', '538835', '538836', '538902', '538921', '538928', '538961', '538962', '538970', '538979', '539006', '539017', '539031', '539041', '539042', '539044', '539045', '539046', '539056', '539083', '539097', '539098', '539099', '539116', '539118', '539126', '539141', '539148', '539150', '539177', '539201', '539216', '539220', '539221', '539222', '539223', '539226', '539227', '539228', '539229', '539251', '539252', '539254', '539265', '539268', '539273', '539275', '539276', '539287', '539289', '539290', '539301', '539302', '539309', '539310', '539312', '539313', '539314', '539331', '539332', '539334', '539336', '539337', '539346', '539359', '539398', '539399', '539400', '539401', '539402', '539403', '539404', '539407', '539428', '539436', '539437', '539447', '539448', '539450', '539480', '539487', '539516', '539517', '539523', '539524', '539526', '539542', '539551', '539570', '539597', '539636', '539658', '539659', '539660', '539678', '539680', '539682', '539686', '539725', '539742', '539760', '539784', '539785', '539787', '539788', '539798', '539799', '539800', '539807', '539837', '539839', '539841', '539843', '539844', '539871', '539872', '539874', '539876', '539883', '539884', '539889', '539917', '539921', '539939', '539940', '539945', '539957', '539963', '539978', '539979', '539980', '539982', '539985', '539986', '539992', '539997', '540005', '540008', '540025', '540027', '540047', '540048', '540061', '540064', '540065', '540072', '540073', '540078', '540079', '540080', '540082', '540084', '540115', '540124', '540125', '540133', '540136', '540144', '540145', '540146', '540147', '540148', '540150', '540151', '540153', '540154', '540173', '540180', '540203', '540205', '540210', '540212', '540222', '540252', '540269', '540293', '540311', '540332', '540358', '540366', '540376', '540377', '540393', '540395', '540396', '540401', '540402', '540403', '540404', '540405', '540416', '540425', '540468', '540492', '540497', '540519', '540530', '540544', '540545', '540550', '540575', '540590', '540595', '540596', '540602', '540611', '540612', '540613', '540614', '540615', '540621', '540642', '540647', '540648', '540649', '540650', '540651', '540652', '540653', '540654', '540669', '540673', '540678', '540679', '540680', '540681', '540691', '540692', '540693', '540694', '540695', '540699', '540700', '540701', '540702', '540704', '540709', '540710', '540715', '540716', '540718', '540719', '540724', '540726', '540727', '540729', '540730', '540735', '540737', '540738', '540743', '540749', '540755', '540756', '540757', '540762', '540767', '540768', '540769', '540774', '540775', '540777', '540778', '540779', '540780', '540781', '540782', '540786', '540787', '540789', '540795', '540796', '540797', '540798', '540809', '540811', '540824', '540843', '540850', '540879', '540900', '540901', '540902', '540923', '540935', '540936', '540937', '540938', '540952', '540953', '540955', '540956', '540961', '540975', '540981', '540982', '540983', '540984', '541006', '541019', '541068', '541069', '541070', '541071', '541083', '541112', '541143', '541144', '541151', '541152', '541153', '541154', '541161', '541163', '541167', '541178', '541195', '541196', '541206', '541228', '541233', '541269', '541276', '541299', '541301', '541302', '541303', '541304', '541313', '541336', '541337', '541338', '541352', '541353', '541402', '541403', '541418', '541444', '541445', '541450', '541540', '541556', '541557', '541578', '541601', '541634', '541700', '541701', '541703', '541729', '541770', '541778', '541799', '541804', '541805', '541806', '541807', '541809', '541865', '541929', '541945', '541956', '541967', '541972', '541973', '541974', '541983', '541988', '542002', '542011', '542012', '542013', '542019', '542020', '542025', '542034', '542046', '542057', '542066', '542131', '542141', '542145', '542146', '542155', '542216', '542230', '542231', '542232', '542233', '542244', '542245', '542246', '542247', '542248', '542285', '542323', '542333', '542337', '542367', '542383', '542399', '542437', '542446', '542459', '542460', '542484', '542513', '542579', '542580', '542592', '542597', '542599', '542628', '542649', '542650', '542651', '542652', '542654', '542655', '542665', '542666', '542667', '542668', '542670', '542678', '542684', '542694', '542721', '542724', '542725', '542726', '542727', '542728', '542729', '542730', '542747', '542752', '542758', '542759', '542760', '542770', '542771', '542801', '542804', '542805', '542806', '542807', '542808', '542809', '542810', '542811', '542812', '542813', '542814', '542815', '542816', '542817', '542818', '542819', '542820', '542830', '542836', '542837', '542838', '542839', '542840', '542841', '542842', '542843', '542844', '542845', '542846', '542847', '542848', '542849', '542850', '542851', '542852', '542857', '542863', '542865', '542867', '542904', '542905', '542907', '542918', '542919', '542920', '542921', '542922', '542924', '542932', '542933', '542934', '542935', '543064', '543065', '543066', '543144', '543145', '543146', '543147', '543148', '543149', '543150', '543151', '543152', '543153', '543154', '543155', '543156', '543168', '543169', '543170', '543171', '543172', '543173', '543174', '543175', '543176', '543177', '543178', '543179', '543180', '543181', '543182', '543183', '543184', '543185', '543186', '543187', '543193', '543209', '543210', '543211', '543212', '543213', '543214', '543218', '543219', '543220', '543221', '543223', '543224', '543226', '543227', '543228', '543230', '543231', '543233', '543234', '543236', '543237', '543238', '543239', '543240', '543241', '543242', '543243', '543244', '543245', '543246', '543248', '543249', '543251', '543252', '543253', '543254', '543255', '543257', '543258', '543259', '543260', '543262', '543264', '543265', '543266', '543270', '543271', '543272', '543273', '543274', '543275', '543276', '543277', '543278', '543279', '543280', '543281', '543283', '543284', '543285', '543286', '543287', '543288', '543291', '543292', '543297', '543298', '543299', '543300', '543305', '543306', '543308', '543309', '543310', '543311', '543312', '543317', '543318', '543319', '543320', '543321', '543322', '543323', '543325', '543326', '543327', '543328', '543329', '543330', '543331', '543332', '543333', '543334', '543335', '543336', '543346', '543347', '543348', '543349', '543350', '543352', '543357', '543358', '543363', '543364', '543365', '543366', '543367', '543372', '543373', '543374', '543375', '543376', '543377', '543383', '543384', '543386', '543387', '543388', '543389', '543390', '543391', '543396', '543397', '543398', '543399', '543400', '543401', '543410', '543411', '543412', '543413', '543414', '543416', '543417', '543419', '543420', '543425', '543426', '543427', '543428', '543433', '543434', '543435', '543437', '543438', '543439', '543440', '543441', '543442', '543444', '543449', '543450', '543451', '543453', '543454', '570001', '570002', '570004', '570005', '590003', '590005', '590006', '590013', '590018', '590021', '590022', '590024', '590025', '590030', '590031', '590041', '590051', '590056', '590057', '590062', '590065', '590066', '590068', '590070', '590071', '590072', '590073', '590075', '590078', '590086', '590134']