# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [v0.12.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.12.0) - 2022-12-23

<small>[Compare with v0.11.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.11.0...v0.12.0)</small>

### Added
- Add system tests for v0.12 ([d3dc777](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d3dc777c567659d8155b5e9e11181b98350753ed) by Simon Kindhauser).
- Add resource type registry to extension api ([37fa9ea](https://gitlab.ost.ch/blackfennec/blackfennec/commit/37fa9ea5f1a60f1ce1ea47b03c452e5c676a26f4) by Caspar Martens).
- Add flatpak templates to extension template ([785af64](https://gitlab.ost.ch/blackfennec/blackfennec/commit/785af64f74a754e9c1c1071d42653f1972c99bea) by Caspar Martens).
- Add introduction to extension development ([ad3d3cb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ad3d3cb3a3d5cee0d8bcb5e8cfddfe20fdc3c569) by Simon Kindhauser).
- Add presentation system index and improve rest of presentation system documentation ([4c4f686](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4c4f686f723528506a2aa21f03c9c1327bb6eb4f) by Caspar Martens).
- Add view documentation ([0895b23](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0895b23ef8b002f638a03cfe82c2b3b243d2692d) by Caspar Martens).
- Add abstract classes for view and view_factory ([e81fafe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e81fafefb856398fba1c118b6a94f2964b316377) by Caspar Martens).
- Add content to study_project increment ([8ad2d4d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8ad2d4d448c89ad39769d1f9c9532ce5b686847c) by Caspar Martens).
- Add domain model documentation ([037fb5a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/037fb5a355c0505ce19d841680d5e2ce12af6354) by Simon Kindhauser).
- Add reflection content ([0beace9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0beace97e21ee37da2e7cf5742d3319208982599) by Caspar Martens).
- Add time tracking content ([41101d9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/41101d92f64896b5dd9cb8dc2bd3f031a372a695) by Caspar Martens).
- Add mirkos changes to abstract ([9bc589f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9bc589f5fa171839981c28de6633a9854b27f7d4) by Caspar Martens).
- Add ux test report for mb ([73e2ef3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/73e2ef3f8f56372a25c6db0facee318ef22e4d45) by Simon Kindhauser).
- Add study project plan ([1278cd1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1278cd18ee2d39aee87d44b4ec01061833b7b405) by Caspar Martens).
- Add a few words to the development docs ([4d193a3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4d193a343f00eb50dcfea6406b14cd23cc025ae4) by Simon Kindhauser).
- Add missing documents to study project section ([5ebb6d0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5ebb6d0c0c376ba77f682d857420eaea92a9a8fd) by Caspar Martens).
- Add reflection, that previously only existed in the project submission ([02fa516](https://gitlab.ost.ch/blackfennec/blackfennec/commit/02fa5167d7644ebc9c425c07c6f5837bf51597b1) by Caspar Martens).
- Add text to docs tests index ([0920512](https://gitlab.ost.ch/blackfennec/blackfennec/commit/09205129cd306d46bfb083aec7bbbd34eb1ef664) by Simon Kindhauser).
- Add usability test result for tw ([a26fd4e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a26fd4e76975eda7f3dd69ea822a8d37c0c62ad0) by Simon Kindhauser).
- Add refs ([e238ff7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e238ff7346c2ca3fd26c0cb7f5202bdbc81bcbbd) by Caspar Martens).

### Changed
- Change histroy to observable layer in domain model ([86d63ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/86d63ca0d9b67b4187118b1c3f71048d6b3862f6) by Simon Kindhauser).
- Change docker project build image tag from gtk4 to latest ([bbc747b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bbc747bc6666ea07caf218aa54beb344d193ba35) by Caspar Martens).

### Fixed
- Fix log level ([a89990b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a89990bd5168b2208aad317f8d6a2240219159c4) by Caspar Martens).
- Fix refs to extension code ([77224f2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/77224f22992217d7dd4e180f5b626bb8f1dac6ce) by Simon Kindhauser).
- Fix the introduction to layers ([2c3c645](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2c3c6451007f62209b4f20974b661a1412bc7b29) by Simon Kindhauser).
- Fix can not create new window with drag and drop ([d81f51b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d81f51b07d77a8b729fe3d50881e27ccdba4094e) by Simon Kindhauser). Related issues/PRs: [#61](ssh://git@gitlab.ost.ch:45022/blackfennec/blackfennec/issues/61)
- Fix toctree ([5cd7eb2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5cd7eb2506b1fc93902c57a0f3df636efcd923c4) by Simon Kindhauser).
- Fix an error when opening tabs ([96f7efb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/96f7efbd53f4078e0e522a675cb0251c8485cb79) by Simon Kindhauser).

### Removed
- Remove broken link to advanced_interpretation ([9b4d6fe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9b4d6fe35f202899db12934b93681aab5cc69455) by Caspar Martens).
- Remove documentation for specification ([f37f958](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f37f9582bc3d7749bd093397c3f12a48235ddb7d) by Simon Kindhauser).


## [v0.11.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.11.0) - 2022-12-14

<small>[Compare with v0.10.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.10.0...v0.11.0)</small>

### Added
- Add system tests ([0a2a00a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0a2a00a7798c7e82dae6b3ce505369d2c95ee157) by Caspar Martens).
- Add abstract, clean up inconsistencies ([6bcb547](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6bcb547de2559318f5936456a4c9d366d23d125a) by Caspar Martens).
- Add extension warning dialog ([eb23348](https://gitlab.ost.ch/blackfennec/blackfennec/commit/eb233480be4831490a4ecf0604576b8d6249b291) by Simon Kindhauser).
- Add links to landing page ([d31394c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d31394c81867aecfd47bb1118673fe5ffad5737d) by Caspar Martens).
- Add tests for paste callback ([4b7166d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4b7166de82d1ebde8aaa661a708ad3cf18059d35) by Caspar Martens).
- Add test for bfvm.open ([f1dc4f1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f1dc4f1e21744bf36225cd6222a21ad6a689882c) by Simon Kindhauser).
- Add paste any mimetype feature ([fba169a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fba169a5a11852dfadec4ca5e5e21b42369201d0) by Caspar Martens).
- Add ui_service tests ([7dcc65a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7dcc65ab02f659cb3903f24d4aabfe2d622fb95a) by Caspar Martens).
- Add message toasts ([1fa0f6a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1fa0f6a820dba0284a0f85347f8c35f31d2d20b0) by Caspar Martens).
- Add ui service with toasting functionality ([5aff20f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5aff20ff75461ebfc5402ba07f9f00cc9d770e9f) by Caspar Martens).
- Add v0.6 and v0.10 and gnome software screenshots ([698ccbd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/698ccbd7e901629bc9d68762be457a5cd451ccb0) by Caspar Martens).
- Add dark/light screenshot ([b8c9b09](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b8c9b095a1481dd3d41ba85ba61ea03973791620) by Simon Kindhauser).

### Changed
- Change issue links and toc ([6179d04](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6179d042cc8b6d5dd9fa33a4001a7cb4dda6367b) by Caspar Martens).

### Fixed
- Fix icon path in readme ([64d3c27](https://gitlab.ost.ch/blackfennec/blackfennec/commit/64d3c271d60ae081bde3e627acc3ab393dde509e) by Simon Kindhauser).
- Fix tests ([c51ac84](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c51ac84e412f051d3cdd115086d8a4d176d1bf84) by Caspar Martens).
- Fix shortcut not functioning in flatpak because of invalid focus ([b226270](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b226270743f3b2683d58f21a3a789063b2568e17) by Caspar Martens).
- Fix scrolling bug ([436ada9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/436ada95a0674b969d65ffe1e7c782078bbbbe5f) by Caspar Martens).
- Fix error when opening context menu, improve opened directory message ([5184fd9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5184fd99080102369c1829c05a9b396cd963a679) by Caspar Martens).
- Fix integration tests ([6e230a7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6e230a7608211fce90df6b2ccae87c446afe0fbb) by Simon Kindhauser).
- Fix dependency graph and flatpak setup ([d2ae0d8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d2ae0d8c1c32d7334c1cd315a08efdf45495c225) by Simon Kindhauser).


## [v0.10.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.10.0) - 2022-11-24

<small>[Compare with v0.9.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.9.0...v0.10.0)</small>

### Added
- Add system tests ([aa3aa7a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/aa3aa7aeeab960bc4a470133ec0029c06646d965) by Caspar Martens).
- Add 0.10.0 old system tests ([8b8b7d7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8b8b7d76e79a360ac1a21d225daba1f6e9bacbdf) by Caspar Martens).
- Add default value for datetime ([714546e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/714546e6f9c0986efea5be81f7e13277ad6c00d1) by Caspar Martens).
- Add merged layer ([b19a982](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b19a982acbf4cf9750c5ca63a23bad3e8bc12b60) by Simon Kindhauser).
- Add layers for overlay and history ([5338219](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5338219f317c67b8e9b8a95d5c2f2ca5042e58df) by Simon Kindhauser).
- Add null view ([ed96a3c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ed96a3cd2db41473f427b997ea90892368400c2e) by Caspar Martens).
- Add paste action and tests ([6723c2c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6723c2c69217f0124b34b3afee5d5b4cfcb1cfe2) by Caspar Martens).
- Add set_structure test ([e7d9725](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e7d9725d1d3cb11e0a344e6a045c853fff764040) by Caspar Martens).
- Add reference encapsulation base ([0ed6cef](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0ed6cefbc84bf87a17a6234897fc1f4f227728e0) by Caspar Martens).
- Add copy feature ([5db81d4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5db81d45b355f5628c47f32402e5daa163eb43bc) by Caspar Martens).
- Add history overlay integration tests ([79c57b6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/79c57b6befa2dd0db8308b8488b1470576b577ee) by Caspar Martens).
- Add history tests ([d51815b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d51815b704efe14826eb802e797c0896abf0b045) by Caspar Martens).
- Add ui undo and redo actions ([17f2ead](https://gitlab.ost.ch/blackfennec/blackfennec/commit/17f2ead9b295d6ee30691b684ca5070ea4cc5511) by Caspar Martens).
- Add change notification tests ([ca6a853](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ca6a853c987cf101753e57ae51b3f6f5b03b9f29) by Caspar Martens).
- Add history layer ([78a773a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/78a773abb44106cf7ea79f10fc877e26700b480f) by Simon Kindhauser).
- Add list and map structure observer item change notification tests ([8a29d98](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8a29d98e3a4fd0c12f077a8af533342dbdc59206) by Caspar Martens).
- Add action tests ([7e761ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7e761ca7199c765884b7918b2bb288fb04745696) by Caspar Martens).
- Add change notification for observable structure ([bff75fe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bff75feec002d5cf890580eaeda1c31d54a0f033) by Caspar Martens).
- Add multi view ([678367d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/678367d43bd01aabacd945a1a884c22e360b585e) by Caspar Martens).
- Add action tests on map and list view models ([0c1023f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0c1023f877331e6d0c7e0485d6ba9df16d0a2e7b) by Caspar Martens).
- Add context menu to action rows ([b52394f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b52394f2860447063e81793db34ffcbf1e37006e) by Caspar Martens).
- Add get_document to document factory ([c7ffdd7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c7ffdd70382975ef6ec41f566f46370fa73533b8) by Simon Kindhauser).
- Add tests for view factory registry ([15ff48a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/15ff48acaff11d2de031afd04bb8d88054b98a3d) by Simon Kindhauser).
- Add tests for view factory ([35dcbd2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/35dcbd22a77dd052e49b1a70ebc9106d2d11cfac) by Simon Kindhauser).
- Add tests for reference ([145ed30](https://gitlab.ost.ch/blackfennec/blackfennec/commit/145ed3076e1a3d858a0206e04c06a212c436b9d4) by Simon Kindhauser).
- Add observable to structure ([a4528fb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a4528fbc44cb68d639a03f8737f745f960c9c5b3) by Simon Kindhauser).
- Add name and description to action ([2a596b3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2a596b38cab9362ba667fdf99a134927247461c0) by Simon Kindhauser).
- Add string actions: to lower and to upper ([baa1cda](https://gitlab.ost.ch/blackfennec/blackfennec/commit/baa1cda7c94fb2345e3f112bf9efe3943d1063bf) by Simon Kindhauser).
- Add action registry to extension api ([5acf7e2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5acf7e2be27620920e619fc05028333673ac0f98) by Simon Kindhauser).
- Add action, registry and context ([ac6e34e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ac6e34ec896323aad6a99ea35af00cbb97d73e66) by Simon Kindhauser).

### Changed
- Change fixed system test status ([85f89ac](https://gitlab.ost.ch/blackfennec/blackfennec/commit/85f89ace1dcd43ecf7995c5abc2d6f1986c45645) by Caspar Martens).

### Fixed
- Fix text insertion bug ([9c9d5ff](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9c9d5ffd7141409d92758e4b09be1c15bd58a0ae) by Caspar Martens).
- Fix image preview not updated when path is invalid ([d99c2d2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d99c2d2195059aad018fb67c56ebd65fe9c1909c) by Simon Kindhauser).
- Fix text entries w.r.t. the history ([26645b9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/26645b9c93b0f9e65d930ec7c598b93255e8e983) by Simon Kindhauser).
- Fix datetime observability ([207698c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/207698c47a9123a072af9438650efd82a337f579) by Caspar Martens).
- Fix diamond problem ([18eeeae](https://gitlab.ost.ch/blackfennec/blackfennec/commit/18eeeae7ead128fc7ef4c261eabfd0d506f150c8) by Simon Kindhauser).
- Fix map_encapsulation parent setting bug ([c2a7c91](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c2a7c910b54a617cb59d8f1ced9bc1bbffff22bb) by Caspar Martens).
- Fix list and list_encapsulation base observabilities ([9c1b0ff](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9c1b0ff49e6770fa3ddc78ae65e164d63edfdab2) by Caspar Martens).
- Fix change notification dispatch missing encapsulation bug ([96d91a8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/96d91a8ca4b835706552a15b0f35f4d931818097) by Caspar Martens).
- Fix import error due to missing init py ([5a3a045](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5a3a045e3800526e2c23e3e0c325db0171ad16d8) by Caspar Martens).
- Fix update_value bug, missing change notification creation ([d400eb1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d400eb187b5afe0c761936ff8667eb015b832d99) by Caspar Martens).
- Fix inconsistencies ([60a1419](https://gitlab.ost.ch/blackfennec/blackfennec/commit/60a141932d459d048420fa30816b230baccdbc05) by Caspar Martens).
- Fix encapsulation base observability dispatch bug ([44f9490](https://gitlab.ost.ch/blackfennec/blackfennec/commit/44f949010fccae4b9fb2773eda8290882c8c19fa) by Caspar Martens).
- Fix reference tests ([fa168ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fa168cae39dd24d07af148183e7938d6094e96c7) by Caspar Martens).
- Fix map editability bug ([58ca762](https://gitlab.ost.ch/blackfennec/blackfennec/commit/58ca762720d8a07ae7a76b8c8ec002aeccb127a5) by Caspar Martens).
- Fix bug in rename_key ([6cab49c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6cab49cff5ede7a69a4e7ed67d90144e0d026b26) by Simon Kindhauser).
- Fix deprecation warnings and type inconsistencies ([7fc53cf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7fc53cf3a381831198698325b086091f18aa0fb2) by Caspar Martens).

### Removed
- Remove setting of log level ([8e60ae6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8e60ae6a5690c5836df93415053203298b5a934f) by Simon Kindhauser).
- Remove number change event on number view instantiation ([7a08af8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7a08af8dd71553186ab593334b8c59acd045aa48) by Caspar Martens).
- Remove boolean change event on boolean view instantiation ([8ebd5a4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8ebd5a48384ae9fd701893b6505c105883deb488) by Caspar Martens).
- Remove defunct delete button ([448f29b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/448f29b6b4b9273ca19db0a52e1bba0b5bc62afd) by Caspar Martens).
- Remove column based presenter extension ([2c2fbd8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2c2fbd85dc6112b478890ccaacc94e7a9d8e29ce) by Simon Kindhauser).


## [v0.9.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.9.0) - 2022-11-04

<small>[Compare with v0.8.1](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.8.1...v0.9.0)</small>

### Added
- Add black fennec view model copy test ([77d94ee](https://gitlab.ost.ch/blackfennec/blackfennec/commit/77d94ee3d1aca67a42d42db9b73c62664890a7a3) by Caspar Martens).
- Add tab attachment and detachment tests ([df14ec5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/df14ec59f94b2458706e694b33a8ffd6c47a9764) by Caspar Martens).
- Add shortcuts, remove settings button ([b5a26b3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b5a26b330edbe61294dca3cf37aaf489abed268a) by Caspar Martens).
- Add authors to about window ([2f8badb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2f8badb4727b52477442be56bc201af34a78fa30) by Caspar Martens).
- Add configuration to pytest.ini and .coveragerc ([0fb3d26](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0fb3d26d6907a4ab9424796ca4ee9e3eda377afc) by Simon Kindhauser).
- Add tests for merge layer ([e8cec20](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e8cec2072ae4ddd3278b56feef278cf5ee5d39b6) by Simon Kindhauser).
- Add about_window ([2de81aa](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2de81aafc0b1f3ef17337fbb42a7613332fda5b6) by Caspar Martens).
- Add presenter tests ([86dc04e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/86dc04e1eb88005376348d0e1027cfff332be3b0) by Caspar Martens).
- Add date_time tests ([03d5959](https://gitlab.ost.ch/blackfennec/blackfennec/commit/03d595985542bcbc9d5e830c5f346b5b718e3d81) by Caspar Martens).
- Add tests for merged list and map ([087614d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/087614d4fcb5308eede331f07809c2bc075f3ec9) by Simon Kindhauser).

### Changed
- Change gio.action registration, add functionality to tab context menu ([a8c5f54](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a8c5f543ddb516824ef7cefcee1a6d6e444814c6) by Caspar Martens).
- Change naming from project to folder ([65394c0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/65394c0b4c6ab32eeb55fc2aa5f188eb246eaf09) by Caspar Martens).
- Change selection class to existing adwaita style class card ([312fcc6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/312fcc6a08682aaa9c3ca771bd0e34feb923cb00) by Caspar Martens).

### Fixed
- Fix invalid appdata ([e674fb5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e674fb503527ee608b4b6e388923b7b4a0a3d94a) by Simon Kindhauser).
- Fix reference serialization bugs ([fbbdfb3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fbbdfb319e9e6e06937b58ddd8092fd10f87e13f) by Caspar Martens).
- Fix save_all oddball solution ([9b4776f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9b4776fb1b82e8a2eb484822423e367210b187bd) by Caspar Martens).
- Fix appdata problem: tag-invalid: <url> type invalid [unknown] ([6651f1b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6651f1bc1d78aad64e544a9cb970d4e9415a456f) by Simon Kindhauser).
- Fix flatpak ([13ec7ab](https://gitlab.ost.ch/blackfennec/blackfennec/commit/13ec7abb06eb60bc0d667d5bc81dc4124d8a2ea4) by Simon Kindhauser).
- Fix close button ([6588d0e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6588d0e8ee5f2b7e2266db90634eaaf7f2fa2838) by Caspar Martens).
- Fix coverage badge ([fb5ec87](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fb5ec878092f1f51107f3745b8639b7a2b9a7cb7) by Simon Kindhauser).
- Fix dockerfile ([5987ea3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5987ea37b6889fa7b00d721381893bb9a40c680a) by Caspar Martens).
- Fix tests ([862cffc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/862cffcfa49aae255a358e93e98c3da36c4c5425) by Caspar Martens).
- Fix reference preview ([0012886](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0012886143dd4d508ff5bf5e8c07348d16b04f60) by Caspar Martens).
- Fix extension_store error ([22a1fb8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/22a1fb86cf304bd56113523feeb36316b284c221) by Caspar Martens).
- Fix bug failing upon showing empty lists ([80ff2fa](https://gitlab.ost.ch/blackfennec/blackfennec/commit/80ff2fa3266fe211df5aaf2d4ec9cdf67be3860e) by Caspar Martens).
- Fix number recursion bug ([972531f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/972531fac68070357e1711f2d62fcf478c9d8525) by Caspar Martens).
- Fix insufficient segregation of ui and non-ui code which caused bug while loading ([322d494](https://gitlab.ost.ch/blackfennec/blackfennec/commit/322d494320b92f832e90cc34a52cfed3fd6eee77) by Caspar Martens).

### Removed
- Remove dependency on appstream ([1aa7df2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1aa7df25286f3b02ed548ff9b30a81403d5e41af) by Simon Kindhauser).
- Remove merged list not implemented warning, test for typeerror when merging incompatible types ([314eef8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/314eef8efe1e6688ee9f6e50dfb91c59f0791392) by Caspar Martens).


## [v0.8.1](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.8.1) - 2022-10-20

<small>[Compare with v0.8.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.8.0...v0.8.1)</small>

### Added
- Add metainfo.xml ([0a67529](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0a675292d9771c93decc223e09a355301229c5eb) by Simon Kindhauser).
- Add tests ([e2c52c5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e2c52c59977076fbb0b65d8122095e90580ce087) by Caspar Martens).
- Add empty list pattern, improve file and project opening ([ee4a8c6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ee4a8c636d2b19dff3bfe3f131b377791f5229e7) by Caspar Martens).
- Add structure access ([103316c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/103316c3113b05ce80e257df370c970407ef6993) by Simon Kindhauser).
- Add install option to makefile ([bfeee83](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bfeee83d1a1bc640cf7c0ad9567bc79a547a2d24) by Simon Kindhauser).
- Add .desktop file ([5cb9b5f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5cb9b5f1976b748fc3053c2631978133316e8740) by Simon Kindhauser).
- Add initial flatpak support ([c6fca22](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c6fca22f40e5668663aa5370c594560736d98b10) by Simon Kindhauser).
- Add mode to load resource api ([84c1916](https://gitlab.ost.ch/blackfennec/blackfennec/commit/84c191644547dc566b7a47c2183d3256eb19c436) by Simon Kindhauser).
- Add valuestructure ([2c2978a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2c2978a81e6250d5f7686cd1977c058f1e93b39a) by Simon Kindhauser).

### Changed
- Change selection class to existing adwaita style class card ([6498cb7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6498cb7fc8e625b42c9ba65d06660db7ba34f58f) by Caspar Martens).
- Change filechooserdialog to filechoosernative for flatpak support ([416a2d5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/416a2d52fa2051ba4796fb6dbec28568c5fa26d6) by Caspar Martens).
- Change flatpak config to use local files ([93ee544](https://gitlab.ost.ch/blackfennec/blackfennec/commit/93ee5446a7ee1c1a10e1105f9230d9b20b598a87) by Simon Kindhauser).

### Fixed
- Fix bug which raised exception when opening a file without project first ([0342d27](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0342d272ff0d65a781b90261df9b5f7cf61b114e) by Caspar Martens).
- Fix build error missing repo ([df4a6b1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/df4a6b1fe239931697b54c4982a6c86045666ee6) by Caspar Martens).
- Fix file, improve image ([e2778f5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e2778f5137a184360c415eda2fbb2fb1fb060b25) by Caspar Martens).
- Fix path in readme ([d6acf7a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d6acf7a1b8d4c1e9c8169c7000fb963ec5d9f43f) by Caspar Martens).

### Removed
- Removed __eq__ from structures ([ad4a7dd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ad4a7dd0e9e0eb3bd042e85b29e06836bb5dd174) by Simon Kindhauser).


## [v0.8.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.8.0) - 2022-10-12

<small>[Compare with v0.5.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.5.0...v0.8.0)</small>

### Added
- Add bftype resource and type loader to extension api ([a0bd85c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a0bd85c6fbeb3be6fdd2fa63c79ac1df6a9a64f7) by Simon Kindhauser).
- Add deep merge and implement inheritance ([0b1cc70](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0b1cc7077527fe14f75c60e9f65623d6a3d2f1d2) by Simon Kindhauser).
- Add type hierarchy ([f1731ad](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f1731adf067e210431883860631826b62df13905) by Simon Kindhauser).
- Add navigator tests ([5de4778](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5de47787a143debcd9b0f70af778e2bb32cef8a9) by Caspar Martens).
- Add null type ([13b6f88](https://gitlab.ost.ch/blackfennec/blackfennec/commit/13b6f88b1d45a7ab0573f42ebfec6bd89205d5c9) by Simon Kindhauser).
- Add tests for number template ([6209072](https://gitlab.ost.ch/blackfennec/blackfennec/commit/620907241e86f30507cf19815fe047cbada598db) by Simon Kindhauser).
- Add template layer ([42df96b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/42df96bd1de2509e3d2874f752b458a509ed763d) by Simon Kindhauser).
- Add styling to base type preview ([aef70c3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/aef70c3dcbf1bcc94b23332fe31508517ddc2d3e) by leonie).
- Add styling to add item row ([abb36ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/abb36ca27a8d68695d0cd4145ab507e63e914478) by leonie).
- Add styling to extension container ([99da9f6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/99da9f6fbb50931bf4e4a29ac7404ca0f735f818) by leonie).
- Add 'add item' row to map ([908daf2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/908daf250e817010087a5809aaee833a92e29d6c) by Simon Kindhauser).
- Add preview for file ([43f1c94](https://gitlab.ost.ch/blackfennec/blackfennec/commit/43f1c94d7c36e93b6af3ca044c059b4c02e5ffd7) by Lara Gubler).
- Add preview for date_time_rage ([a8ccbf1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a8ccbf18b15079b403c1b13ba96e6494ce16ca66) by Lara Gubler).
- Add name to tempaltes for user firendly identifiers ([57e2dd3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/57e2dd372f9348cc50095aeecb0c37d644d7c6b3) by Simon Kindhauser).
- Add preview for image ([9403fdf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9403fdf33e635890463d7aff111923dffd6a85bb) by Lara Gubler).
- Add person preview ([d698b46](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d698b46844a60891548790923b984c48536f4ba8) by Lara Gubler).
- Add extension store tests ([b761ea3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b761ea3a1b61384f16e43ae445fce01f50d234fe) by leonie).
- Add preview for date_time ([ef695fa](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ef695faac81c26b8f51a0fd08841d737111c05d9) by Lara Gubler).
- Add extension store ([74e14ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/74e14caa48fe22b7bed63ba81654a2a4fd1691bf) by leonie).
- Add create_structure to template ([f0b24cb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f0b24cba1739655c55e9e56430191e77be2090ae) by Simon Kindhauser).
- Added quit functionality ([8339179](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8339179dd7197a2186664e7e001cbe575d082822) by leonie).
- Add refinement task descriptions ([567c295](https://gitlab.ost.ch/blackfennec/blackfennec/commit/567c295cd3c7798b00892106f1e6e78997e85f2a) by Caspar Martens).
- Add description to some refinement tasks ([fcdabd3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fcdabd3f131e33cef5ba69668331bc730fbf0591) by Caspar Martens).
- Added review feedback ([60d5dec](https://gitlab.ost.ch/blackfennec/blackfennec/commit/60d5dec8aee89b962d32f3bf927a1682af1502ce) by leonie).
- Added project plan feedback ([a243178](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a243178c16b1dce498b3c783e58a6f209702b838) by leonie).
- Add refinement documentation ([69a7901](https://gitlab.ost.ch/blackfennec/blackfennec/commit/69a7901de33ba536d300b780600ac50dc25d0976) by Lara Gubler).
- Add systemtests for release v0.6 ([f16ce91](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f16ce916221c4353534e89abee4dd60df386a2ee) by Lara Gubler).
- Add participant to usability tests ([8113bff](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8113bff820e469f7daceb9f939bf65c3d18e6168) by Caspar Martens).
- Add usability testing part1 ([0d6612a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0d6612ac61e8d97b822741a23837def35790b4bd) by Simon Kindhauser).
- Add performance test with huge type extension ([1a129f9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1a129f95d06f704db8b3532bd820986e3609e0db) by Caspar Martens).
- Add templates to map add wizard ([db5f969](https://gitlab.ost.ch/blackfennec/blackfennec/commit/db5f969e0d01902ad5065db285884cf8a301445d) by Simon Kindhauser).
- Added fallback font ([2dc3110](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2dc3110e5b82cbbafbc19d61b4438e039f3c4f29) by leonie).
- Adde dextension view ([db685dc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/db685dcf799af20c41bfdc05a6d3315d12d4a396) by leonie).
- Add ux tests ([dcaabfe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/dcaabfe75d04668d789159730c49e3cb758d9ee7) by Caspar Martens).
- Add performance system test ([927a700](https://gitlab.ost.ch/blackfennec/blackfennec/commit/927a7006df3936a4c8681e34fca1f826f6a5313b) by Caspar Martens).
- Added extension store ui ([7e3ec39](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7e3ec390bb769400935aaf03822aea5a398aeebd) by leonie).
- Add templateregistry lookup in list view add item ([0743ef7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0743ef715ebd4579d2661ab8a6bbbd0363aa4118) by Caspar Martens).
- Add template registry ([4e217ea](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4e217ea669417137c42afb6123894119534a2f0d) by Caspar Martens).
- Added style to menu item ([4ad68de](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4ad68de29e3957d6a888856570add4062de81d6c) by leonie).
- Add sequence diagrams ([a7e371e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a7e371ec3ef63b26ffa1917e7fa373d0586a7c0d) by Simon Kindhauser).
- Add extension store view model ([e958944](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e95894443112763907db18e39d837ba48394a150) by Caspar Martens).
- Add save functionality for project ([ffc39c1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ffc39c1ead5ddc6fee6fb1e229cae408c0bdb8bb) by Simon Kindhauser).
- Add term-missing option to test ([10446cd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/10446cd3cc633184cdf8ca6126d3482bef510eed) by Caspar Martens).
- Add coverage tests, fix pylint ([2150d97](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2150d97a8950fd669019b4460a6218deb3a9b472) by Caspar Martens).
- Add deps, test and run to make file ([9ba2928](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9ba2928705991fd74532bee89c4121b69e1c6575) by Simon Kindhauser).
- Add tests ([ba99f47](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ba99f4772b3b113a83bb330d7dd0bc3c28ef2c94) by Caspar Martens).
- Added styling to window controls ([ddd76ba](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ddd76ba11650e783b005d5d2cf4c164be1c9e3be) by leonie).
- Added window icon ([d3db060](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d3db0606a75bd17bfd5a37c41274445926bd5bb3) by leonie).

### Changed
- Change required python version to 3.10 ([d458199](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d4581996bd01254132dc24e6deda9de2a911bc49) by Caspar Martens).
- Change coloring ([2c5d7c2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2c5d7c2787933f46f65a29816e9c3e7865a6d71c) by Caspar Martens).
- Change ux test hierarchy ([e5208a5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e5208a5e7a97e278fd7801b6663726c96b09db7c) by Caspar Martens).

### Fixed
- Fix list not hashable ([1cd35e0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1cd35e0203ce265baa547aae9691c04539c5abab) by Simon Kindhauser).
- Fix links in readme ([7c23ba3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7c23ba3f45c5ccb2523b2185fdb5537ad9ae17ce) by Caspar Martens).
- Fix some linting warnings ([e6d9d95](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e6d9d9583b4d338e5db8aa70c68853ef80fc440d) by Simon Kindhauser).
- Fix black fennec application ([5e0290a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5e0290af6bb6566cb3aecb88a69be8e486577ef6) by Caspar Martens).
- Fix errors ([6b6d90b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6b6d90b790e72bb29d2ad439490f23322e94e95f) by Caspar Martens).
- Fix list and map equality bug ([3eb0d93](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3eb0d935c462ef4d3a194b1eb7a2af741a161d24) by Simon Kindhauser).
- Fix linter warnings ([a714b29](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a714b299c36024cc7b4179630661d99b5ab86285) by Simon Kindhauser).
- Fix using subject instead of self.subject ([b9a718f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b9a718f902a786f9930241b0e452fb5d6b8b0b19) by Simon Kindhauser).
- Fix multi-encapsulation issues ([62eafef](https://gitlab.ost.ch/blackfennec/blackfennec/commit/62eafeffeb0bc789f27c2b61f2827d35b8d21a88) by Simon Kindhauser).
- Fix dangerous-default-value (w0102) ([17aa4cf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/17aa4cf0509c380113cb63235f2ae89fcbc9b5e0) by Simon Kindhauser).
- Fix oddball_solution in registires ([128a5e8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/128a5e8443d8367f6cb70b432ed19153c403703a) by Simon Kindhauser).
- Fix test case ([833618d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/833618d60d362b54b784ec07a7e0a30cdcf33a7a) by Simon Kindhauser).
- Fix 'line too long' ([f7d747c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f7d747ca79d88e2deb5122ac2e25d435cd80d027) by Simon Kindhauser).
- Fix path error of extensions.json ([d43deb0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d43deb0bbfa862c4ba86ba1980eb4044c9054874) by Caspar Martens).
- Fix pylint errors ([76daf23](https://gitlab.ost.ch/blackfennec/blackfennec/commit/76daf23d82b735e8c19ef2b1ae1cea8f48421ea9) by Caspar Martens).
- Fix typo in boolean_view ui template ([67cf743](https://gitlab.ost.ch/blackfennec/blackfennec/commit/67cf743b7e1bc525650ac91516cfd7cf83b61670) by Caspar Martens).
- Fix new tabs open in background ([8a6e246](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8a6e246d8a068e2d2aaf70dec6749525159eb5d9) by Simon Kindhauser).
- Fix redundant click handler in reference preview ([322d81c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/322d81ceeae9009b66657116b859a71d0e53ee61) by Simon Kindhauser).
- Fix factory satisfies specificaiton tests for base types ([7ab341d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7ab341db12e3fa62e5530901f513d349b5621d64) by Simon Kindhauser).
- Fixed out of focus popup font color ([d5f4166](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d5f4166fab28d33eb573591cad6fcfc5ab9005a2) by leonie).
- Fix notify observers on map key rename ([1bbab1a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1bbab1a30cfa2897bedf5f7c1724167da2b3aa70) by Simon Kindhauser).
- Fixed pipeline ([bd214fe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bd214fed733cb7e59ced14d96c97f8f5e051b3d0) by leonie).
- Fix sphinx warnings ([8b496d6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8b496d6d2defbfe256c5d909723a10decf9a22c3) by Caspar Martens).
- Fix #161 ([521d32d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/521d32dce7508a2dd116038a20f39598e3068d70) by Caspar Martens).
- Fixed boolean bug ([fef4382](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fef438215c34a52d2e65f7c8443f372b881925da) by leonie).
- Fixed handle position ([1274942](https://gitlab.ost.ch/blackfennec/blackfennec/commit/12749429ccbadba9a5373dede20746b134f546d3) by leonie).

### Removed
- Remove json_reference_resoling_service double ([f3f3823](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f3f3823d7e135bdb1211820ba7a90acbf97bb57c) by Caspar Martens).
- Remove uri library incompatible with python 3.10 last traces ([87915ad](https://gitlab.ost.ch/blackfennec/blackfennec/commit/87915adbe9b30da79e1715ee37a39667db2f4f59) by Caspar Martens).
- Remove uri library incompatible with python 3.10 ([5a2a32e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5a2a32ea1e9242188e97b1be852c8c4b3d152675) by Caspar Martens).
- Remove napoleon ([6432be6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6432be65878fe8fe447022d5f77dcba9499ced78) by Simon Kindhauser).
- Remove dead code ([934c0c6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/934c0c68a69ec8eca0729770ff9cabfdf79bcf3d) by Caspar Martens).
- Remove unused member interpretation._view ([20dc0ee](https://gitlab.ost.ch/blackfennec/blackfennec/commit/20dc0ee0228982310588948ab71bc599f845ee01) by Simon Kindhauser).
- Remove hash function; speculative generality ([c5f7b25](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c5f7b25320f73f2c10393074d28d9a2ea34e35de) by Caspar Martens).
- Remove set loglevel ([63b8af8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/63b8af8fe5785ece5a231c3879bb000db63cb709) by Caspar Martens).
- Remove 'add' option from row context menu ([6af65b3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6af65b3650da30e6bf24a2bc03291971f6e9242a) by Simon Kindhauser).
- Remove userdict/userlist/userstring ([6f378c6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6f378c6d9f26f510bd60af94e612f393476122a4) by Caspar Martens).
- Remove one refinement task ([ff6da5c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ff6da5c039ff8121c313ad7cee70828bcb67b834) by Caspar Martens).
- Remove children property from structure ([ba777e3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ba777e3b181246b2e928486bf184edabb4c65bb2) by Caspar Martens).
- Remove class constaint for visit_list, visit_map, visit_string ([274b7d9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/274b7d91432f75ad06ba123ac6b5497c95954378) by Caspar Martens).
- Remove primitive-obsession of coverage ([3d57207](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3d5720707ab77feda1ddb9d410fc59353b4be25a) by Caspar Martens).


## [v0.5.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.5.0) - 2021-05-19

<small>[Compare with v0.3.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.3.0...v0.5.0)</small>

### Added
- Add system tests ([e9b8fde](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e9b8fde4461dc122eef9b236258ea648f2a2fc9d) by Lara Gubler).
- Add delete and add actions to list ([765b11a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/765b11a3f4e2ea8bcb03c81912a10b1c69672483) by Simon Kindhauser).
- Added editable map ([4f58773](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4f587730b1ff4a96081ff2121232aff3b08569eb) by leonie).
- Add destroy of extensions, change presenter-/type-registry deregister to accept types instead of instances ([2679ad7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2679ad7e74370ac6f47fcc7576c66583ca11d301) by Caspar Martens).
- Add extension development documentation ([79c0aff](https://gitlab.ost.ch/blackfennec/blackfennec/commit/79c0affee50d99b5e72b84763cb59bf4ae545a70) by Caspar Martens).
- Add link to ui/ux design decisions ([b1eef72](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b1eef72dcdf85814eb17b449f1da49cb741cc96b) by Simon Kindhauser).
- Add editable map ([efccf4d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/efccf4da933a07d63f2656093cf4214b36142f5d) by Lara Gubler).
- Add pretty print for extensions.json ([057eb4e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/057eb4e6b4ac2c25a501ad57e6a1f7c87d3c4018) by Caspar Martens).
- Added close function to notebook pages ([ac7a217](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ac7a2176e676b4cb246ebe00c081e5e98afc9b32) by leonie).
- Add architecture review overview page ([894b443](https://gitlab.ost.ch/blackfennec/blackfennec/commit/894b4433390561e8e99c78e7076ef02d99f22ff2) by Simon Kindhauser).
- Added tab system ([7e7605d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7e7605d796408ffa1b073c875734bd30d9690945) by leonie).
- Add architecture and design documentation overview ([c451c47](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c451c471caacbd825f0a2fb87e75a39de5e9d088) by Lara Gubler).
- Added default image size and resize feature ([3ec92c9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3ec92c96c2cedc6fa312ab766644d20b580d291d) by leonie).
- Add extension management logic ([c85ccb2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c85ccb2434b71751d76489189f0fe80a1732a96a) by Caspar Martens).
- Add tests for home_address and personal_photo properties ([6c3c138](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6c3c1383368bddd858263540f60d56454c9e49b3) by Caspar Martens).
- Added state change animation to boolean ([d8210fb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d8210fbd72b4c9f94cc0a5a54736a5e040e4dace) by leonie).
- Added column styling ([7a2291b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7a2291b7e7a4fb21192b4d7301221882bcfbac9c) by leonie).
- Add docstrings ([094cb7f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/094cb7f2a81a6b4dfeb205dc54756826a3ac7183) by Caspar Martens).
- Added scrolling and resize feature to columns ([de6d244](https://gitlab.ost.ch/blackfennec/blackfennec/commit/de6d244bcc79b031b8754cbb7b6202b55a24871d) by leonie).
- Added title icons to base ([534119a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/534119a6af8696e83f7035eb889a57de0614ea37) by leonie).
- Added resize feature to main containers ([f721048](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f721048635e4ae2229c26db616e5e143437a5e60) by leonie).
- Added base styling ([35193cb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/35193cb899444a0933f0e0f275986e8466252eda) by leonie).
- Added styling to core types ([71de074](https://gitlab.ost.ch/blackfennec/blackfennec/commit/71de074e0f57a1da970d00411815137ec1b77fa3) by leonie).
- Add filter ([cb3df21](https://gitlab.ost.ch/blackfennec/blackfennec/commit/cb3df21e8954a7296d9ac481e992beb9415f7a0a) by Caspar Martens).
- Add overlay tests ([03fb612](https://gitlab.ost.ch/blackfennec/blackfennec/commit/03fb612d797c6f8700d811d74545a5d878120fd5) by Caspar Martens).
- Add template tests ([944856b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/944856bff036682f046888dbc0418df4be99eb1d) by Caspar Martens).
- Add overlay and template ([4caa2f8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4caa2f8667cb8959368fca4e1e4af6413471ac25) by Caspar Martens).
- Add jsonreferenceresolvingservice tests ([06a0716](https://gitlab.ost.ch/blackfennec/blackfennec/commit/06a0716e05b83cca894eba1ec558e944d5526b62) by Caspar Martens).
- Add jsonpointer tests ([e11d79e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e11d79e9e6204aed0d4021fba69f8abfd60026ec) by Caspar Martens).
- Add reference tests ([bc5ae8d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bc5ae8de1471e7565f16a699d44b3b11942be41b) by Caspar Martens).
- Added system test template ([9591e64](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9591e64533a9499d8308c3022834d09ab744e3e0) by leonie).
- Added styling ([71afcfd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/71afcfdda9662f291aa7c0b32a93ea08519d47d5) by leonie).
- Added file tree view ([c7c4232](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c7c42325962bc12bcafb0be5dc5af0371db85942) by leonie).
- Add interpretation_service to black_fennec.py ([9b56df6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9b56df63a8e15061c393c93d60e52d1c26023613) by Lara Gubler).
- Add preview for core type boolean ([e22cb28](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e22cb288394f8731d4569a9d9ca3f64b0498cf31) by Lara Gubler).
- Add preview for core type number ([c94c974](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c94c9746a97dc6b2c9316bed53ed0f20d96e6f67) by Lara Gubler).
- Add preview for core type list ([533701d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/533701d0f6ac6d42fd3395da4bbcce72cea1b40a) by Lara Gubler).
- Added active highlight ([b1faa1c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b1faa1cc6a010e956ee2cb9b1c1595efcd65de5d) by leonie).
- Added image padding ([3c5ebeb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3c5ebeb903925ebc78bf57b1bb5773cf2748415e) by leonie).
- Added ui/ux documentation ([9f7f5d5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9f7f5d5e6dcf5900770cecb4d7e2a48e175efa45) by leonie).
- Add reference coretype, fileimportservice, jsonreferenceresolvingservice, jsonpointer ([8342492](https://gitlab.ost.ch/blackfennec/blackfennec/commit/834249236a4df0c2e188a12325c353a141d9026a) by Caspar Martens).
- Added highlight on active elements ([b494e43](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b494e4313d1c1ab4de9561ef08a83c32036ee896) by leonie).
- Addes basic styling ([e7369d7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e7369d79a63de854839827cacc118091fdac03c0) by leonie).
- Added css according to ui sketches ([aa41fdb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/aa41fdb116a8c93c30ce83ccc90209302b1b8f41) by leonie).
- Add documentation to create_preview function in map_view_model, fix docstrings ([83629dd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/83629dd5bfa789c8794f09949985a9ba3ca6d0e1) by Simon Kindhauser).
- Added extension mccabe and docsparam to pylint ([c5d37d1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c5d37d1851182f99ada02ec1b126d5b9dfaa414d) by Caspar Martens).
- Add preview for core types map and string ([99b9994](https://gitlab.ost.ch/blackfennec/blackfennec/commit/99b9994129e150a144861ba84bd23e0d167c252c) by Simon Kindhauser).
- Add test for specification ([0ba501f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0ba501f1caebe4298eb5c93a6a3ae102b5b8a879) by Simon Kindhauser).
- Add specification ([65c7b09](https://gitlab.ost.ch/blackfennec/blackfennec/commit/65c7b09219f20ceecd84b72f13f2e315f007041e) by Simon Kindhauser).
- Add basic styling ([e06941d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e06941dd9bea6db9c663814e6e1099b35f2923f8) by leonie).
- Add base type date_time, add date_time unit tests ([9a04de2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9a04de29a05574522aa4acbf0431332e71ff8ece) by Lara Gubler).
- Add file example ([1b9221f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1b9221fab57081deb9ee9861302afed1586067c6) by Caspar Martens).
- Add string value regex matching for template ([66607cb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/66607cb8f87ca71a747d3584e89adb7192281268) by Caspar Martens).
- Add base type image ([00b2a71](https://gitlab.ost.ch/blackfennec/blackfennec/commit/00b2a71e8554aa3d72fc73cc0f437da6f7c930ff) by Caspar Martens).
- Add file base type ([b8d313d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b8d313d765a5d09e3270dc82c20b48d05d8aee90) by Caspar Martens).
- Add test cases ([7d9cd6a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7d9cd6ad3e7b36b6ddacdcaa214471706d30c082) by leonie).
- Add base typ person ([830206d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/830206d8f04382964006b07a139bcb0221ee161d) by leonie).
- Add person.py core type properties ([5fd135c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5fd135c3fa78599fb04241fbd46f0f79b5dec5dc) by leonie).

### Changed
- Change version number ([6ac0c63](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6ac0c633f77bc02e969ad387a3ff7731d50451db) by Caspar Martens).
- Change local import of type_system/presenter extensions ([a513a44](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a513a440c7df965b5a1ecf39d08b08c664271bb3) by Caspar Martens).
- Change info message to be representative ([a235be1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a235be1e12aa49fe20c28bd00ccd4c9ac5c22a3d) by Caspar Martens).
- Change function name in string_view.py ([5220d30](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5220d3027e2e3978e343aa22e89d3170f04b57e9) by Lara Gubler).
- Change core type boolean to be editable ([784bde3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/784bde3cab268546774cf44aa71c59a6521ad7c3) by Lara Gubler).
- Change core type number to be editable ([5b950ad](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5b950adf0897197cc433a98c701d520a7e16932d) by Lara Gubler).
- Change structure ([4d60d39](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4d60d397bb15205c18cc6976253e41fa024c2908) by Simon Kindhauser).
- Change printscale from weekly to daily ([8901f46](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8901f4681e07bf50425c4781d1e8b17bc539e7da) by Caspar Martens).

### Fixed
- Fix some linter issues ([e6025e9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e6025e90dd78142dce10744babf61051b67e3e51) by Simon Kindhauser).
- Fix glade paths ([efc65ed](https://gitlab.ost.ch/blackfennec/blackfennec/commit/efc65edf27e3ce91d9859496ce27b99af50ea6ca) by Caspar Martens).
- Fix path join bug in create_folder_structure ([d877b30](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d877b3058a7bdb28aa65b4497738ea63d5c83ed1) by Simon Kindhauser).
- Fix path join bug in create_fodler_strucutre ([08c4b80](https://gitlab.ost.ch/blackfennec/blackfennec/commit/08c4b8068eff9c493de62773a20936e6f9abfc7d) by Simon Kindhauser).
- Fix type ([cad0da0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/cad0da0d732fca0950c4c61a1be698448909a38d) by Simon Kindhauser).
- Fix make docs error ([88b8d7e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/88b8d7eeed24ae5a6022185f61167d3cf36dea4c) by Caspar Martens).
- Fixed pipeline ([80e1809](https://gitlab.ost.ch/blackfennec/blackfennec/commit/80e180945b29320d7ed968cad54a018d85ab0b73) by leonie).
- Fixed integration test for localextensionservice ([a5c26dc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a5c26dcfa18767ae2825612857bb5dfc15654f54) by Caspar Martens).
- Fixed failed test ([e96d749](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e96d749d43130827967546deb09f8911b3132185) by leonie).
- Fix pylint ([c019047](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c0190472efd3ccf8a5046b13e628cefc88a9dff2) by Caspar Martens).
- Fixed details ([ab39368](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ab39368cf4258405405378f6aaf3f1e71d27458e) by leonie).
- Fix according to review ([f4d2e51](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f4d2e515552b7d1c7f8e6f1f175350ea50d62c7f) by Caspar Martens).
- Fixed pipeline and legacy code ([d31f714](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d31f714647c4fe192cdb9ece336d4654d6b5b78e) by leonie).
- Fix pylint, except for missing docstrings ([2d01d4a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2d01d4ab7a7f4fec08110fb7c996574001d23bfd) by Caspar Martens).
- Fix file tree multi column bug ([56ae124](https://gitlab.ost.ch/blackfennec/blackfennec/commit/56ae124684c305aa64fedb559cda789047cb0649) by Simon Kindhauser).
- Fix pylint except docstrings warnings ([6fdbbb5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6fdbbb5bdcb8eea36315c78d38cb412bdf4a81d1) by Caspar Martens).
- Fix double paths ([445b04e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/445b04e1a693242562f16c59b00e91021ea31a81) by Caspar Martens).
- Fix docstrings and other pylint issues ([55b6371](https://gitlab.ost.ch/blackfennec/blackfennec/commit/55b6371c5a07174f0a06d71de11691c175f684bd) by Caspar Martens).
- Fix pylint merge conflict ([76b7712](https://gitlab.ost.ch/blackfennec/blackfennec/commit/76b771277ab48832ac1dbe5d07822ae56469deb4) by Caspar Martens).
- Fixed window focus bug ([18dedd2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/18dedd28668e123b81e4e3f1d63d45a11e906540) by leonie).
- Fix linter warnings ([708efd1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/708efd1037184bfff6f59ccf433fa8b47cf95ebf) by Simon Kindhauser).
- Fixed backgrounds ([ec157bd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ec157bd2c32ef9f744f85135f1164c43bfd97b68) by leonie).
- Fix pylint in basetype person ([a4f2c51](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a4f2c51d1efc060a279c29015aa4308d489f532d) by Caspar Martens).
- Fix image offer comparison to file/map offer tests ([90a8c74](https://gitlab.ost.ch/blackfennec/blackfennec/commit/90a8c749048e2fd690d25f98c396d5d11a134bf0) by Caspar Martens).
- Fix pipeline ([5cb82f1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5cb82f1f584d25273f793e0dee7686df4e15e02e) by leonie).
- Fix merge and pylint issues ([dd73d92](https://gitlab.ost.ch/blackfennec/blackfennec/commit/dd73d92a61cfb36ca33d4a6cf9f2b662f3640076) by Caspar Martens).

### Removed
- Remove version build because of gitlab space limitations ([0a2a69d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0a2a69d51b3d30c6dee410ef23cbf4551f8bd6d7) by Caspar Martens).
- Remove combotest file, remove unused import, fix double template ([73a720c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/73a720c191e7562ab4157eba2e4fdb0ed4280159) by Simon Kindhauser).
- Remove map initialisation in encapsulation ([e29fb0b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e29fb0bb97c74a7db2b57b2b94da074db7ffc304) by Caspar Martens).
- Remove access on data property ([142f9c5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/142f9c53f5befc5907a31b03e1b7d178dfc8c0fd) by Caspar Martens).
- Remove iteration abbreviation ([e9fe048](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e9fe0484272a699ac5230262481b3db0c8682eb0) by Caspar Martens).


## [v0.3.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.3.0) - 2021-04-13

<small>[Compare with v0.2.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.2.0...v0.3.0)</small>

### Added
- Add links to code docs ([1aa95d6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1aa95d6debc8c4bf05fcb0cb6858ae7232f1dca4) by Caspar Martens).
- Add updated time charts ([2eb5b24](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2eb5b2480df67c15189d0c0caf77d16a84d7096f) by Caspar Martens).
- Add imagebuild stage before prebuild ([5228119](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5228119de332734b4c1a208aaffaf3c2c1c27fe0) by Caspar Martens).
- Add docs generation prebuild task ([6cdbc24](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6cdbc24671ac1b308adeccbe89563419dfcc8485) by Caspar Martens).
- Add construction phase roadmap ([0de964a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0de964a04225f87f9bc53aa6ab815ca99af92d7e) by Caspar Martens).
- Add elaboration overview ([13b064b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/13b064b2e4d0c5dbbfcdaeba9d18a1652bea4878) by Caspar Martens).
- Add address type to type registry ([5f70ff4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5f70ff4754601a94068b3ba266a6ec644f06514b) by Caspar Martens).
- Add automatic code docuementation generation ([18ada7d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/18ada7d2c4bf3aa3727a1428e4b66611a8d470ee) by Simon Kindhauser).
- Add integration tests ([e9c69d1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e9c69d10015e54e30ef5958d11e3073a7e5b0b36) by Lara Gubler).
- Add address base type with tests ([ad1c64e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ad1c64e769ad956223108b3d777efec7b6bbde2c) by Caspar Martens).
- Add testing to index ([9680500](https://gitlab.ost.ch/blackfennec/blackfennec/commit/968050029a2e9e7fe561a3a99faa105286586553) by leonie).
- Add template file ([3ae92a5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3ae92a5262671f9264148d5fb69b3220867f6f5c) by leonie).
- Add future test cases ([c7e594c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c7e594c9ed5172b9f4516913a5be27a00f3f4bd5) by leonie).
- Add documentation of architecture ([4aa4fed](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4aa4fed613a27f70cad6be3a7a8ea36ac57f688c) by Simon Kindhauser).
- Add bar chart to time_tracking.py ([7449ccf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7449ccf11222e1cb8dc00522ea9c3f353dcd4eee) by Lara Gubler).
- Add system test cases ([d815447](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d815447ec2691c9a8c3ae9fd028d31f864b02deb) by leonie).
- Add template parameter to offer ([26b07f8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/26b07f89cd6c9d83437cf1fe7cf90f0f0b14da7e) by Caspar Martens).
- Add boolean tests ([553a58a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/553a58a8fa78be75adf94573aea696588fdc308d) by Caspar Martens).
- Add resizing and drag feature ([5e6f734](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5e6f7341394cef363ee3805d6cb3af9266c34b71) by leonie).
- Add alternative font ([35084c4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/35084c44cbd7b86dfdac111b2bb24bc25fa15c17) by leonie).
- Add observable tests ([d0ebe2b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d0ebe2badce37f05805a54f839b99a5748ef5be1) by Caspar Martens).
- Add column based presenter tests ([0026d8b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0026d8b9ec33dd5ddd1e58fd35a3b58ff090696c) by Caspar Martens).
- Add test for auctioneer with no offers ([6bc9352](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6bc9352ed9a1c42597f6783b4b74322a6adc08f8) by Caspar Martens).
- Added file selector ([be6fd50](https://gitlab.ost.ch/blackfennec/blackfennec/commit/be6fd50e31cfd17a9883cd18c764c77b938500ca) by leonie).
- Added splash screen ([cdf1df7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/cdf1df79198c42e1586e862a9cbd828f5174f4f4) by leonie).
- Add json_encoder, test_json_encoder.py, reformat list.py ([762acb7](https://gitlab.ost.ch/blackfennec/blackfennec/commit/762acb70e1c3239b339115caf19c556d4f3c6601) by lara.gubler).
- Add test cases ([7a9c950](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7a9c950294a932126ff0d3cb734d7ef355ea47f3) by leonie).
- Add comments ([6db9963](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6db99634c921af0fc3b2804596309d5e41adf242) by leonie).
- Add click handler ([c2ab88b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c2ab88b9a1abd2a7e12337baf5bb455c6faf20a6) by leonie).
- Add json_parser.py and test_json_parser.py ([4cba174](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4cba174bbae47b88457969782566d9c1107434ec) by lara.gubler).
- Add some more documentation ([3a27915](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3a27915695aa1a05865e8967884f9bc021628cf9) by Simon Kindhauser).
- Add main ui ([0c025a4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0c025a4cae71b9848152ca066cc07b383dba4bb7) by leonie).
- Add column based presenter ([412ad33](https://gitlab.ost.ch/blackfennec/blackfennec/commit/412ad338a94505acc006cc9d2cd7f503d970bdeb) by Caspar Martens).
- Add docstrings to auctioneer ([92f9ecc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/92f9eccaab8cfb2f5bc5f1471ab126a28f26f90f) by Caspar Martens).
- Add navigation service with testing ([de1ec1e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/de1ec1e75d0f5a01f6414d63e7cbdcb5a42f1000) by Caspar Martens).
- Add auctioneer with testing ([3c19e80](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3c19e80a406f9e504faf5e8ba34973f72a0e1d23) by Caspar Martens).
- Add comparable tests, correct pylint offer tests ([7a1df66](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7a1df66ecaf90304b2fd4cfed913cb07d01d8687) by Caspar Martens).
- Add types to interpreter and interpretation ([d20da0f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d20da0fa22deae77c1cf3f636496d1fb44eb3258) by Caspar Martens).
- Add offer tests ([cf62354](https://gitlab.ost.ch/blackfennec/blackfennec/commit/cf623549b2bfbba2db39f91776542b3a4ca5c566) by Caspar Martens).
- Add children to core info ([f2b162f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f2b162f5e3828919b5433830fe186a805b62cc08) by Simon Kindhauser).
- Add core type boolean ([bec5fc4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bec5fc41652bff3ec832216887a1479112b88f1c) by Simon Kindhauser).
- Add core type number ([5c08cc2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5c08cc257ebab3ee59f63eb5edcb1573bfc7904c) by Simon Kindhauser).
- Add core type list ([b808797](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b80879747018aa30f444e169ee473ba27a4982ad) by Simon Kindhauser).
- Add offer ([4114bbe](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4114bbeb0e00a049a152cdbf8d1edaeda8293afa) by Caspar Martens).
- Add comparable ([518b2e2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/518b2e2621a7151786c249b7e88744b610181f2e) by Caspar Martens).
- Add core type map view ([154b479](https://gitlab.ost.ch/blackfennec/blackfennec/commit/154b4796f1b5a4184c2f508d1923bbf85284219b) by Simon Kindhauser).
- Add core type map view model, fix tests ([7583bc9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7583bc9ffc557080b14ab4ef899be7065894960d) by Simon Kindhauser).
- Add core type map bidder ([bcffc80](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bcffc8007c6d47607c91c8d553f1c562c60eecca) by Simon Kindhauser).
- Add core type map ([7ffa062](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7ffa0628815ab4cd53a9bbdd0e41353b90881d32) by Simon Kindhauser).
- Add docstrings to type_registry.py ([62aae98](https://gitlab.ost.ch/blackfennec/blackfennec/commit/62aae98719b0b47a10f9ab63f88fcb910d11a604) by Lara Gubler).
- Add test cases for type_registry ([18230f2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/18230f2f3491c859a90d27823767da3641d0f67d) by Lara Gubler).
- Add string view model and view factory tests and fix bugs ([89564dc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/89564dc1521bb71a5382b7d403b8d6882befb455) by Simon Kindhauser).
- Add string view factory ([0699513](https://gitlab.ost.ch/blackfennec/blackfennec/commit/06995131749865c42926a80fabb69ce7dbee020b) by Simon Kindhauser).
- Add test_type-registry.py ([d76f40a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d76f40a28d6a5a46047d021cc9ed084a8564a92a) by Lara Gubler).
- Add string view and view model ([733dc4c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/733dc4ce3b0913bbf91dd6b764d416da923054db) by Simon Kindhauser).
- Add returns and attributes to docstring ([f8eb2d9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f8eb2d99204d132bf57a0378f693026592ac1a4d) by Caspar Martens).
- Add docstrings to core type root ([78384ea](https://gitlab.ost.ch/blackfennec/blackfennec/commit/78384eacd63eebd121a4b996cd24e0cbd8dab2c9) by Simon Kindhauser).
- Add docstring to core type info ([44ab2bb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/44ab2bb854086773ab6334081c2cd0fcc30a7833) by Simon Kindhauser).
- Add docstrings to core string ([cdcdf57](https://gitlab.ost.ch/blackfennec/blackfennec/commit/cdcdf576198d14a9c333ce1e4d100f6a603fb546) by Simon Kindhauser).
- Add type-registry ([c7c6ff6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c7c6ff61da8016b07ca551ab8c4a624050b50564) by Lara Gubler).
- Added ci_cd to index.rst ([ce6e40b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ce6e40b6eb658b7c3b24ca2ccf22fe9c2dc84c59) by leonie).
- Add interpreter and interpretation ([3d67f69](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3d67f696cb9f49725b2992149884c7476f4ffa0a) by Caspar Martens).
- Add string bidder ([b2903bd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b2903bdf2ddb03920c9fc306911559f49c192da9) by Simon Kindhauser).
- Add string ([aafddfa](https://gitlab.ost.ch/blackfennec/blackfennec/commit/aafddfacb918d97ae6d1a6c847e14b55e9270b50) by Simon Kindhauser).
- Add root ([27fcc93](https://gitlab.ost.ch/blackfennec/blackfennec/commit/27fcc9355aca2ccc4c678b6292af5c08b2228b8b) by Simon Kindhauser).
- Add info ([d370942](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d370942c90d99c4ae25dcedad00e2b34900af17c) by Simon Kindhauser).

### Changed
- Change offer interface ([4ef4c18](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4ef4c184c3249e0d1d11409b4023ea7f4d6ae3b0) by Caspar Martens).
- Change interpretation info_view argument to [info_view] ([52734d6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/52734d62118a3db51cd5170fa5827a97da0d442e) by Caspar Martens).
- Change version number ([58fed1b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/58fed1b6faab089ea3f575877a74a6fd7f901a80) by Caspar Martens).

### Fixed
- Fix code docs artifacts ([145369b](https://gitlab.ost.ch/blackfennec/blackfennec/commit/145369b26729bfb54cc3f67bd5c81cb861a32637) by Caspar Martens).
- Fix linting ([1ac98c9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1ac98c9744a12a6fe925f3af00d4e3ccc49c4f77) by Simon Kindhauser).
- Fix pylint ([de0f273](https://gitlab.ost.ch/blackfennec/blackfennec/commit/de0f2738d36bc30e24d6dd0d3058a04c944d7c27) by Caspar Martens).
- Fix 'no offer is best offer' for type boolean #113 ([5428d43](https://gitlab.ost.ch/blackfennec/blackfennec/commit/5428d438aaf3ff1216ed4ac64f969bf919a25bc3) by Simon Kindhauser).
- Fix version number and project information ([165a875](https://gitlab.ost.ch/blackfennec/blackfennec/commit/165a875a25dac9db106e853b0d797df684d49393) by Simon Kindhauser).
- Fixed typos and added tbd ([e6c86bd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e6c86bd636be92f9a187d9c9426cc1f4f394abc7) by leonie).
- Fix testsuite names ([51d35c1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/51d35c1bece55e9f5b30ee9d367251e1a568224d) by Caspar Martens).
- Fix bug recognized during system testing and add regression unit-test ([a745a72](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a745a72eeeb0e18fb7c2285a3c6923b14eea65a3) by Caspar Martens).
- Fix pylint warnings ([ae5df84](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ae5df84554812c22afeb3d584fe1183e7cd305e5) by Caspar Martens).
- Fix tests for black fennec view model ([607567c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/607567c0d9b99f104c9ef4c6c8f8ff99b13d3067) by Simon Kindhauser).
- Fix splash screen timer ([7f48628](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7f486287369640019056b8e775f119f15b96834c) by Simon Kindhauser).
- Fix issues from merge ([978dad8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/978dad8b1e3017a777991a3349fbd13d2bcfa909) by Simon Kindhauser).
- Fixed pipeline ([beaae48](https://gitlab.ost.ch/blackfennec/blackfennec/commit/beaae48834e9cad4abfdd24f1295ca98ae93d6f7) by leonie).
- Fix unit tests ([ca3ff64](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ca3ff64c00953b9ccce33c888c1c6b828040ac65) by Simon Kindhauser).
- Fix core type unittests after integration ([b7e2a73](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b7e2a737978630860b7e70e73a36b220dbc1f722) by Simon Kindhauser).
- Fix logic error in comparable ([8792ddb](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8792ddb5fd52bea97abcd6b02b471633e9ec90a8) by Caspar Martens).
- Fixes and renamings ([1dfdea9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1dfdea9f13344a1bee50644133b9584481307987) by Simon Kindhauser).
- Fix pipeline the second ([629fff2](https://gitlab.ost.ch/blackfennec/blackfennec/commit/629fff292d64ab1c15b6c8ce6a72c6ed6ce973de) by Simon Kindhauser).
- Fix pipe line for gtk gui testing ([902de26](https://gitlab.ost.ch/blackfennec/blackfennec/commit/902de260930f89220adb63a43a7eacb4f254bbe6) by Simon Kindhauser).
- Fix format in time tracking scripts ([b5c02e4](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b5c02e497895c3bb06131c0e7768af9f9c073f06) by Caspar Martens).

### Removed
- Remove navigation_service dependency from auctioneer ([45606ae](https://gitlab.ost.ch/blackfennec/blackfennec/commit/45606ae95338ce2fca886da287edb0d56b3cc44f) by Caspar Martens).


## [v0.2.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.2.0) - 2021-03-23

<small>[Compare with v0.1.2](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.1.2...v0.2.0)</small>

### Added
- Add time_tracking ([f76db1c](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f76db1c04abdb73bbf9a95d5c0cd0c8202c495d8) by Lara Gubler).
- Add time_tracking.py ([8691ed0](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8691ed0f73a771f9fd39d3b4e4518a2615d6d825) by Lara Gubler).
- Add domain concept type registry ([f22dacc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/f22dacc6482cb7ae8d6f646214e593e095cd85ba) by Simon Kindhauser).
- Add domain model overview v1.0 ([b647b11](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b647b111cd25ce963a2efee6840993399b5e4eec) by Simon Kindhauser).
- Add domain concept navigation ([8538cde](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8538cdeafd74ef109735ec9d07627cb32089028e) by Simon Kindhauser).
- Add domain documentation for layers ([69c9edc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/69c9edc6b2d21ee8c4652075edfe1fdb4f8be0dc) by Simon Kindhauser).
- Add ui sketches ([d8b0ebc](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d8b0ebc6d5dc29f53e3ef6fbc37e2a02a556496b) by Lara Gubler).
- Add personas, add overview descriptive text ([229b6f3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/229b6f383ef07e9ceb958606a4a8cc88a4e4781a) by Caspar Martens).
- Add spacing below tables ([118a061](https://gitlab.ost.ch/blackfennec/blackfennec/commit/118a061feef555fa8cca7ee7cb4c5e9624a36579) by Caspar Martens).
- Add non-functional requirements ([bd86a94](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bd86a94943ac626a040f816d6cc195d326b06817) by Caspar Martens).
- Add seletion process to domain model ([7a54103](https://gitlab.ost.ch/blackfennec/blackfennec/commit/7a5410359586a9fa02b50d8e58f32496baf811e4) by Simon Kindhauser).
- Add non-function requirements ([21d7dba](https://gitlab.ost.ch/blackfennec/blackfennec/commit/21d7dbafd4625e7d49cf06f59632683f80112e65) by Caspar Martens).
- Added table to describe nfrs ([8a2477e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/8a2477eb52ee10bf0a2c507bc5567d8ed806dc8d) by Caspar Martens).
- Add some non-functional requirements ([9b7e278](https://gitlab.ost.ch/blackfennec/blackfennec/commit/9b7e2787363ce5bdff73cc494ab0269e230450e6) by Simon Kindhauser).
- Add non-functional requirements skeleton ([6d77b17](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6d77b175fc0bd29d43ae616b4340fb6e1fdb160d) by Caspar Martens).

### Changed
- Change version number ([fe53517](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fe53517c415bfa03c55ec0ec7cc8953f6a40b84a) by Caspar Martens).
- Change ui_sketches order ([0def401](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0def4011adcc32e19c7a15e7d1d019673ef1dd70) by Caspar Martens).

### Fixed
- Fixed based on feedback ([3825f0f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3825f0f58d0b087afc5e9ad6ddeed10aec512f3d) by Simon Kindhauser).


## [v0.1.2](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.1.2) - 2021-03-15

<small>[Compare with v0.1.1](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.1.1...v0.1.2)</small>

### Added
- Add _versions path to gitignore ([a7c5166](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a7c5166aec583ea68375b173ea4c9a2bce168417) by Caspar Martens).
- Add svg2pdf converter ([e276373](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e27637377fe5c7a91ee545a2ddd0ae1e32f4ce04) by Caspar Martens).
- Add time conversion script ([b0bffed](https://gitlab.ost.ch/blackfennec/blackfennec/commit/b0bffede4b42acdbb6cef6b0562fd0599f7fb02f) by Simon Kindhauser).
- Add new directory ([4614327](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4614327c84bc433a823860e96f77b73e788900f4) by Lara Gubler).
- Add usecase overview ([2924d3f](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2924d3ffb7311be13cb9b2175ad79383a9b8da83) by Caspar Martens).
- Add linting to ci, reformat source-code to comply with linting ([1b344c5](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1b344c5b012b94fcefbd7e62e00c919126808658) by Caspar Martens).


## [v0.1.1](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.1.1) - 2021-03-09

<small>[Compare with v0.1.0](https://gitlab.ost.ch/blackfennec/blackfennec/compare/v0.1.0...v0.1.1)</small>

### Added
- Add time tracking ([3dde5c1](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3dde5c1e188ae099d376dfa72c54ac65cab98b24) by Caspar Martens).


## [v0.1.0](https://gitlab.ost.ch/blackfennec/blackfennec/tags/v0.1.0) - 2021-03-09

<small>[Compare with first commit](https://gitlab.ost.ch/blackfennec/blackfennec/compare/19acd71b11ee93d1accba6eb541b6d6d11a64d3b...v0.1.0)</small>

### Added
- Add documentation guidelines ([715a0e3](https://gitlab.ost.ch/blackfennec/blackfennec/commit/715a0e374b80a3f3c45349b66ab1a2d2104d5291) by Caspar Martens).
- Add subsection testing to qa ([6c3b167](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6c3b16789fdd5cbfb660fa4f7c3521e5f11efe47) by Caspar Martens).
- Add subsection development to quality assurance ([47c20af](https://gitlab.ost.ch/blackfennec/blackfennec/commit/47c20af621604294b0bbd79d267384435dbb02f3) by Caspar Martens).
- Add high level documentation on extensions ([95b1742](https://gitlab.ost.ch/blackfennec/blackfennec/commit/95b1742f2ec377bda5e9dc02ac31fab03315b76e) by Simon Kindhauser).
- Add docs extensions/index ([1f00079](https://gitlab.ost.ch/blackfennec/blackfennec/commit/1f0007994be078819e82c3ce4d5f13f3c3464a82) by Simon Kindhauser).
- Add version control strategy ([2fe38ca](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2fe38cabdc79e4338249955156ebe57ae1200b5e) by Caspar Martens).
- Add risk analysisi ([3777c10](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3777c10f481752778ce91371d2a03a584a998fb0) by Simon Kindhauser).
- Add time management, move meetings ([a951d01](https://gitlab.ost.ch/blackfennec/blackfennec/commit/a951d01fb430e3e5560c8598458feb27971240f0) by Caspar Martens).
- Add definition of done, add logging standards ([e92d5d6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/e92d5d6fa5193844840fe2de6faf0339bab376f3) by Simon Kindhauser).
- Added subsection scope of delivery, iteration planning, releases, meetings and protocolling ([87b7d15](https://gitlab.ost.ch/blackfennec/blackfennec/commit/87b7d15736aba41dd67b89cbd6813e4137f01a1b) by lara.gubler).
- Add project organisation, project management ([fdabd75](https://gitlab.ost.ch/blackfennec/blackfennec/commit/fdabd7587e25959582f7cdb9c57d90696a88c278) by Caspar Martens).
- Add project overview ([6c1063d](https://gitlab.ost.ch/blackfennec/blackfennec/commit/6c1063d4352a7667f4d8d876fc08592322ff65ff) by Caspar Martens).
- Add hello world ([2051e13](https://gitlab.ost.ch/blackfennec/blackfennec/commit/2051e13922dcca9cc633188deca5e4e551fc5026) by Simon Kindhauser).
- Add apt package texlive and librsvg ([54cbf18](https://gitlab.ost.ch/blackfennec/blackfennec/commit/54cbf185191815039fff84764f87aae0427960d3) by Caspar Martens).
- Add additional apt dependency required to build pygobject ([ddacd55](https://gitlab.ost.ch/blackfennec/blackfennec/commit/ddacd556fca97893e90fbe79867b5f00ca8d61e0) by Caspar Martens).
- Add requirement pygobject ([df9cd6e](https://gitlab.ost.ch/blackfennec/blackfennec/commit/df9cd6e4270f3a1c065f0392d254134d55ffbec2) by Caspar Martens).
- Add setup.py and tests ([554d8a6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/554d8a67318c90367961ae53d5c69f6885fc1938) by Caspar Martens).
- Add gitlab-ci configuration ([410131a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/410131a835297af1532f69871dac10e135ef35aa) by Caspar Martens).
- Add project proposal (german) ([07d97fa](https://gitlab.ost.ch/blackfennec/blackfennec/commit/07d97fab616487a04adcfad52c475d87fdd8cbdc) by Simon Kindhauser).
- Add make docs ([aaa73cf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/aaa73cfed85ae62ab3bcb77d14c86803c89b45ca) by Simon Kindhauser).

### Changed
- Change titles of risks in risk analysis ([0757caf](https://gitlab.ost.ch/blackfennec/blackfennec/commit/0757cafa83c776155083ddba1938984c1a34b335) by Simon Kindhauser).
- Change apt get package librsvg to librsvg2-bin ([bb309f6](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bb309f6950ddad0623d4d946dd99a508c2cd1c49) by Caspar Martens).
- Changed image base to not alpine, because gtk does not run on alpine ([4eda65a](https://gitlab.ost.ch/blackfennec/blackfennec/commit/4eda65a956bc7ae65ebba90cc191c5414abd6e63) by Caspar Martens).
- Changed apk installs ([d3b1219](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d3b121957a2ae1fecc5876c421d44fa17e047cd3) by Caspar Martens).

### Fixed
- Fix typo ([bf66518](https://gitlab.ost.ch/blackfennec/blackfennec/commit/bf665186bccd0460a7d286dbb8e73482ba690df2) by Simon Kindhauser).
- Fix typos and table widths ([d754656](https://gitlab.ost.ch/blackfennec/blackfennec/commit/d7546568660cefa0ed04dbceae21a88de3a4a1d6) by Simon Kindhauser).
- Fix milestone links ([13acfc9](https://gitlab.ost.ch/blackfennec/blackfennec/commit/13acfc9ae261c0c7ea631b6efc7f5d9630a557c4) by Caspar Martens).
- Fix milestone table ([c77b238](https://gitlab.ost.ch/blackfennec/blackfennec/commit/c77b238566d549d797035cfdebb1a218f5861757) by Caspar Martens).
- Fix typo in logging_standards ([66106d8](https://gitlab.ost.ch/blackfennec/blackfennec/commit/66106d84ae628567d6d2c5b5ae0f732cd48d34b8) by Simon Kindhauser).
- Fix spelling mistake, fix .gitignore ([3a6ac95](https://gitlab.ost.ch/blackfennec/blackfennec/commit/3a6ac956adc09b4a3fe7dcdde05aa3c49471dbad) by Caspar Martens).
- Fix makefile source directory path ([de79afd](https://gitlab.ost.ch/blackfennec/blackfennec/commit/de79afd81e345f1d1b4183e3008348c46cab21f6) by leonie.daeullary).
- Fixed yaml indentation ([438ea76](https://gitlab.ost.ch/blackfennec/blackfennec/commit/438ea76c23c8337a63f795bd35b63a2fcdc764a1) by Caspar Martens).

### Removed
- Remove trailing slashes in regex ([6535599](https://gitlab.ost.ch/blackfennec/blackfennec/commit/65355998d315152cbb3f2450cea2a38840e76941) by Caspar Martens).


