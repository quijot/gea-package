--
-- Data for Name: circunscripcion; Type: TABLE DATA 
--

COPY circunscripcion (id, nombre, orden) FROM stdin;
1	Santa Fe	Primera
2	Rosario	Segunda
\.


--
-- Data for Name: dp; Type: TABLE DATA 
--

COPY dp (dp, nombre, habitantes, superficie, cabecera, circunscripcion_id) FROM stdin;
1	9 de Julio	28273	16870	Tostado	1
2	Vera	51303	21096	Vera	1
3	General Obligado	166436	10928	Reconquista	1
4	San Javier	29912	6929	San Javier	1
5	Garay	19913	3964	Helvecia	1
6	San Justo	40379	5575	San Justo	1
7	San Cristóbal	64935	14850	San Cristóbal	1
8	Castellanos	162165	6600	Rafaela	1
9	Las Colonias	95202	6439	Esperanza	1
10	La Capital	489505	3055	Santa Fe	1
11	San Jerónimo	77253	4282	Coronda	1
12	San Martín	60698	4860	Sastre	1
13	Belgrano	41449	2386	Las Rosas	2
14	Iriondo	65486	3184	Cañada de Gómez	2
15	San Lorenzo	142097	1867	San Lorenzo	2
16	Rosario	1121441	1890	Rosario	2
17	General López	182113	11558	Melincué	2
18	Caseros	79096	3449	Casilda	2
19	Constitución	83045	3225	Villa Constitución	2
\.


--
-- Data for Name: ds; Type: TABLE DATA; 
--

COPY ds (id, dp, ds, nombre) FROM stdin;
1	1	1	G.P.DE DENIS
2	1	2	GATO COLORADO
3	1	3	SAN BERNARDO
4	1	4	POZO BORRADO
5	1	5	TOSTADO
6	1	6	LOGROÑO
7	1	7	ESTEBAN RAMS
8	1	8	MONTEFIORE
9	1	9	JUAN DE GARAY
10	1	10	VILLA MINETTI
11	1	11	SANTA MARGARITA
12	2	2	VERA
13	2	3	LA GALLARETA
14	2	4	MARGARITA
15	2	5	CALCHAQUI
16	2	6	TOBA
17	2	7	FORTIN OLMOS
18	2	8	CAÑADA OMBU
19	2	9	GOLONDRINA
20	2	10	INTIYACO
21	2	11	GARABATO
22	2	12	LOS AMORES
23	2	13	TARTAGAL
24	3	2	FLORENCIA
25	3	3	EL RABON
26	3	4	V GUILLERMINA
27	3	5	LAS TOSCAS
28	3	6	S A DE OBLIGADO
29	3	7	TACUARENDI
30	3	8	VILLA OCAMPO
31	3	9	VILLA ANA
32	3	12	ING CHANOURDIE
33	3	13	EL SOMBRERITO
34	3	14	ARROYO CEIBAL
35	3	15	LAS GARZAS
36	3	16	LANTERI
37	3	19	AVELLANEDA
38	3	20	RECONQUISTA
39	3	21	EL ARAZA
40	3	22	BERNA
41	3	23	MALABRIGO
42	3	24	LOS LAURELES
43	3	26	LA SARITA
44	3	27	GUADALUPE NORTE
45	3	28	NICANOR MOLINA
46	4	1	ROMANG
47	4	2	COLONIA DURAN
48	4	3	ALEJANDRA
49	4	4	SAN JAVIER
50	4	5	C ARIACAIQUIN
51	4	6	LA BRAVA
52	5	1	HELVECIA
53	5	2	CAYASTA
54	5	3	SANTA ROSA
55	5	5	COLONIA MASCIAS
56	5	6	SALADERO CABAL
57	6	1	P GOMEZ CELLO
58	6	2	LA CAMILA
59	6	3	VERA Y PINTADO
60	6	4	S MARTIN NORTE
61	6	5	LA CRIOLLA
62	6	6	LA PENCA-CARAG.
63	6	7	CRESPO
64	6	8	SILVA
65	6	9	M. ESCALADA
66	6	10	RAMAYON
67	6	11	SAN JUSTO
68	6	12	NARE
69	6	13	SAN BERNARDO
70	6	14	ANGELONI
71	6	15	VIDELA
72	6	16	ESTHER
73	6	17	CAYASTACITO
74	6	18	COLONIA DOLORES
75	7	1	CERES
76	7	2	HERSILIA
77	7	3	AMBROSETTI
78	7	4	HUANQUEROS
79	7	5	LAS AVISPAS
80	7	6	AGUARA
81	7	7	V SARALEGUI
82	7	8	SAN CRISTOBAL
83	7	9	SANTURCE
84	7	10	PORTUGALETTE
85	7	11	ARRUFO
86	7	12	LA RUBIA
87	7	13	COLONIA ANA
88	7	14	VILLA TRINIDAD
89	7	15	COLONIA ROSA
90	7	16	SAN GUILLERMO
91	7	17	CURUPAYTI
92	7	18	CAPIVARA
93	7	19	ANDUCITA
94	7	20	LA LUCILA
95	7	21	LA CLARA
96	7	22	SOLEDAD
97	7	23	CONSTANZA
98	7	24	MOISES VILLE
99	7	25	MONIGOTES
100	7	26	SUARDI
101	7	27	MTE OBSCURIDAD
102	7	28	COL DOS ROSAS
103	7	29	COLONIA BOSSI
104	7	30	LAS PALMERAS
105	7	31	PALACIOS
106	7	32	LA CABRAL
107	8	1	VIRGINIA
108	8	2	MAUA
109	8	3	HUMBERTO I
110	8	4	COL.RAQUEL
111	8	5	TACURAL
112	8	6	TACURALES
113	8	7	BICHA
114	8	8	EUSEBIA
115	8	9	HUGENTOBLER
116	8	10	ALDAO
117	8	11	SUNCHALES
118	8	12	ATALIVA
119	8	13	GALISTEO
120	8	14	LEHMAN
121	8	15	EGUSQUIZA
122	8	16	BIGAND
123	8	17	FIDELA
124	8	18	PBLO.MARINI
125	8	19	RAMONA
126	8	20	CNEL.FRAGA
127	8	21	VILA
128	8	22	COL CASTELLANOS
129	8	23	PTE ROCA
130	8	24	RAFAELA
131	8	25	BELLA ITALIA
132	8	26	AURELIA
133	8	27	SUSANA
134	8	28	VILLA SAN JOSE
135	8	29	SAGUIER
136	8	30	SAN ANTONIO
137	8	31	S C DE SAGUIER
138	8	32	BAUER Y SIGEL
139	8	33	JOSEFINA
140	8	34	COL.CELLO
141	8	35	CLUCELLAS
142	8	36	COL.ITURRASPE
143	8	37	ANGELICA
144	8	38	EST CLUCELLAS
145	8	39	EUSTOLIA
146	8	40	ZENON PEREYRA
147	8	41	FRONTERA
148	8	42	ESMERALDA
149	8	43	GARIBALDI
150	8	44	MARIA JUANA
151	8	45	COL.MARGARITA
152	8	46	SAN VICENTE
153	9	1	ELISA
154	9	2	JACINTO L ARAUZ
155	9	3	LA PELADA
156	9	4	ITUZAINGO
157	9	5	SOUTOMAYOR
158	9	6	PROVIDENCIA
159	9	7	MARIA LUISA
160	9	8	SANTO DOMINGO
161	9	9	PROGRESO
162	9	10	HIPATIA
163	9	11	SARMIENTO
164	9	12	FELICIA
165	9	13	GRUTLY
166	9	14	RIVADAVIA
167	9	15	CULULU
168	9	16	ESPERANZA
169	9	17	COL.CAVOUR
170	9	18	HUMBOLT
171	9	19	NUEVO TORINO
172	9	20	PILAR
173	9	21	STA M CENTRO
174	9	22	STA MARIA NORTE
175	9	23	SAN GMO NORTE
176	9	24	LAS TUNAS
177	9	25	PUJATO NORTE
178	9	26	FRANK
179	9	27	EMP.SAN CARLOS
180	9	28	COL.SAN JOSE
181	9	29	SAN AGUSTIN
182	9	30	SAN Carlos NORTE
183	9	31	SAN G DEL SAUCE
184	9	32	SA PEREIRA
185	9	33	SAN MARIANO
186	9	34	STA C B VISTA
187	9	35	SAN Carlos CENTRO
188	9	36	MATILDE
189	9	37	SAN CARLOS SUD
190	10	1	EMILIA
191	10	2	CABAL
192	10	3	LLAMBI CAMPBELL
193	10	4	CPO.ANDINO
194	10	5	LAGUNA PAIVA
195	10	6	NELSON
196	10	7	CANDIOTI
197	10	8	ARROYO AGUIAR
198	10	9	MONTE VERA
199	10	10	RECREO
200	10	11	SANTA FE
201	10	12	SANTO TOME
202	10	13	SAUCE VIEJO
203	10	15	ARROYO LEYES
204	10	16	S J DEL RINCON
205	11	1	LOPEZ
206	11	2	GESSLER
207	11	3	LARRECHEA
208	11	4	DESVIO ARIJON
209	11	5	CORONDA
210	11	6	LOMA ALTA
211	11	7	CAMPO PIAGGIO
212	11	8	GALVEZ
213	11	9	SAN EUGENIO
214	11	10	AROCENA
215	11	11	SAN FABIAN
216	11	12	IRIGOYEN-PUEBLO
217	11	13	B DE IRIGOYEN
218	11	14	CASALEGNO
219	11	15	BARRANCAS
220	11	16	MONJE
221	11	17	GABOTO
222	11	18	MACIEL
223	11	19	ESTACION DIAZ
224	11	20	S.GENARO NORTE
225	11	21	SAN GENARO
226	11	22	CENTENO
227	12	1	CASTELAR
228	12	2	CRISPI
229	12	3	SASTRE
230	12	4	S M DE LAS ESC
231	12	5	COL BELGRANO
232	12	6	CAÑADA ROSQUIN
233	12	7	TRAILL
234	12	8	SAN JORGE
235	12	9	LAS PETACAS
236	12	10	LANDETA
237	12	11	C PELLEGRINI
238	12	12	CASAS
239	12	13	LAS BANDURRIAS
240	12	14	LOS CARDOS
241	12	15	EL TREBOL
242	12	16	PIAMONTE
243	12	17	MARIA SUSANA
244	13	1	BOUQUET
245	13	2	LAS ROSAS
246	13	3	LAS PAREJAS
247	13	4	MONTES DE OCA
248	13	5	TORTUGAS
249	13	6	ARMSTRONG
250	14	1	CLASON
251	14	2	TOTORAS
252	14	3	CARRIZALES
253	14	4	OLIVEROS
254	14	5	PUEBLO ANDINO
255	14	6	SERODINO
256	14	7	LUCIO V LOPEZ
257	14	8	SALTO GRANDE
258	14	9	BUSTINZA
259	14	10	CDA DE GOMEZ
260	14	11	CORREA
261	14	12	VILLA ELOISA
262	15	1	TIMBUES
263	15	2	PTO S MARTIN
264	15	3	SAN LORENZO
265	15	4	FRAY L BELTRAN
266	15	5	CAP BERMUDEZ
267	15	6	RICARDONE
268	15	7	ALDAO
269	15	8	LUIS PALACIOS
270	15	9	CARCARAÑA
271	15	10	S JERONIMO SUR
272	15	11	ROLDAN
273	15	12	PUJATO
274	15	13	CNEL ARNOLD
275	15	14	FUENTES
276	15	15	VILLA MUGUETA
277	16	1	IBARLUCEA
278	16	2	G BAIGORRIA
279	16	3	ROSARIO
280	16	4	FUNES
281	16	5	ZAVALLA
282	16	6	PEREZ
283	16	7	SOLDINI
284	16	8	V GDOR GALVEZ
285	16	9	ESTACION ALVEAR
286	16	10	PIÑERO
287	16	11	ALVAREZ
289	16	13	ACEBAL
290	16	14	C DEL SAUCE
291	16	15	C DOMINGUEZ
292	16	16	VILLA AMELIA
293	16	17	GRAL LAGOS
294	16	18	ARROYO SECO
295	16	19	FIGHIERA
296	16	20	CNEL BOGADO
297	16	21	ALBARELLOS
298	16	22	PUEBLO URANGA
299	16	23	ARMINDA
300	16	25	PUEBLO ESTHER
301	17	1	CAFFERATA
302	17	2	LA CHISPA
303	17	3	MURPHY
304	17	4	CHOVET
305	17	5	CDA DEL UCLE
306	17	6	FIRMAT
307	17	7	MIGUEL TORRES
308	17	8	CARRERAS
309	17	9	MELINCUE
310	17	10	ELORTONDO
311	17	11	CARMEN
312	17	12	CHAPUY
313	17	13	VENADO TUERTO
314	17	14	SAN FRANCISCO
315	17	15	MAGGIOLO
316	17	16	SAN EDUARDO
317	17	17	MARIA TERESA
318	17	18	SANTA ISABEL
319	17	19	VILLA CAÑAS
320	17	20	HUGHES
321	17	21	LABORDEBOY
322	17	22	WHEELWRIGHT
323	17	23	TEODELINA
324	17	24	SAN GREGORIO
325	17	25	CHRISTOPHERSEN
326	17	26	SANCTI SPIRITU
327	17	27	RUFINO
328	17	28	LAZZARINO
329	17	29	A CASTELLANOS
330	17	30	DIEGO DE ALVEAR
331	17	31	AMENABAR
332	18	1	ARTEAGA
333	18	2	S J ESQUINA
334	18	3	AREQUITO
335	18	4	LOS MOLINOS
336	18	5	CASILDA
337	18	6	SANFORD
338	18	7	BIGAND
339	18	8	CHABAS
340	18	9	VILLADA
341	18	10	L QUIRQUINCHOS
342	18	11	BERABEVU
343	18	12	CHAÑAR LADEADO
344	18	13	GODEKEN
345	19	1	BOMBAL
346	19	2	ALCORTA
347	19	3	JUNCAL
348	19	4	MAXIMO PAZ
349	19	5	PAVON ARRIBA
350	19	6	SANTA TERESA
351	19	7	LA VANGUARDIA
352	19	8	CEPEDA
353	19	9	SARGENTO CABRAL
354	19	10	PEYRANO
355	19	11	SANCHEZ
356	19	12	GENERAL GELLY
357	19	13	J B MOLINA
358	19	14	GODOY
359	19	15	RUEDA
360	19	16	EMP V CONSTIT
361	19	17	THEOBALD
362	19	18	V CONSTITUCION
363	19	19	PAVON
288	16	12	PUEBLO MUÑOZ
\.


--
-- Name: ds_id_seq; Type: SEQUENCE SET; 
--

SELECT setval('ds_id_seq', 363, false);


--
-- Data for Name: lugar; Type: TABLE DATA; 
--

COPY lugar (id, nombre, obs) FROM stdin;
1	Pueblo MATILDE	\N
2	Zona Rural de SANTA CLARA DE BUENA VISTA	\N
3	Ciudad de ROSARIO	\N
4	Colonia GÁLVEZ	\N
5	Zona Rural de GÁLVEZ	\N
6	Ciudad de GÁLVEZ	\N
\.


--
-- Name: lugar_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 
--

SELECT setval('lugar_id_seq', 6, true);


--
-- Data for Name: objeto; Type: TABLE DATA; Schema: public; Owner: 
--

COPY objeto (id, nombre) FROM stdin;
1	Mensura
\.


--
-- Name: objeto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 
--

SELECT setval('objeto_id_seq', 1, true);


--
-- Data for Name: sd; Type: TABLE DATA; Schema: public; Owner: 
--

COPY sd (id, ds, sd, nombre) FROM stdin;
1	1	0	\N
2	2	0	\N
3	3	0	\N
4	4	0	\N
5	5	0	\N
6	6	0	\N
7	7	0	\N
8	8	0	\N
9	9	0	\N
10	10	0	\N
11	11	0	\N
12	12	0	\N
13	12	1	OGILVIE
14	12	2	ESPIN
15	12	3	CARAGUATAY
16	12	4	SANTA FELICIA
17	12	5	SANTA LUCIA
18	13	0	\N
19	14	0	\N
20	15	0	\N
21	16	0	\N
22	16	1	GUAYCURU
23	17	0	\N
24	17	1	KM29-F.GUAYCURU
25	18	0	\N
26	19	0	\N
27	19	1	LOS TABANOS
28	20	0	\N
29	20	1	COLMENA
30	21	0	\N
31	21	1	KM 101
32	22	0	\N
33	23	0	\N
34	24	0	\N
35	24	1	ISLAS
36	25	0	\N
37	25	1	ISLAS
38	26	0	\N
39	27	0	\N
40	27	1	ISLAS
41	28	0	\N
42	29	0	\N
43	30	0	\N
44	30	1	ISLAS
45	31	0	\N
46	31	1	LA RESERVA
47	32	0	\N
48	33	0	\N
49	33	1	ISLAS
50	34	0	\N
51	34	1	ISLAS
52	35	0	\N
53	35	2	ISLAS
54	36	0	\N
55	36	1	FLOR DE ORO
56	37	0	\N
57	37	2	ESTACION MOUSSY
58	37	3	ISLAS
59	38	0	\N
60	38	1	ISLAS
61	39	0	\N
62	40	0	\N
63	41	0	\N
64	42	0	\N
65	42	1	ISLAS
66	43	0	\N
67	43	1	SAN MANUEL
68	44	0	\N
69	44	1	ISLAS
70	45	0	\N
71	46	0	\N
72	46	1	ISLAS
73	47	0	\N
74	48	0	\N
75	48	1	ISLAS
76	49	0	\N
77	49	1	ISLAS
78	49	2	COLONIA TERESA
79	50	0	\N
80	51	0	\N
81	52	0	\N
82	52	2	ISLAS
83	53	0	\N
84	53	1	ISLAS
85	54	0	\N
86	54	1	ISLAS
87	55	0	\N
88	55	1	ISLAS
89	56	0	\N
90	56	1	ISLAS
91	57	0	\N
92	58	0	\N
93	59	0	\N
94	60	0	\N
95	61	0	\N
96	62	0	\N
97	63	0	\N
98	64	0	\N
99	65	0	\N
100	66	0	\N
101	67	0	\N
102	68	0	\N
103	69	0	\N
104	70	0	\N
105	71	0	\N
106	72	0	\N
107	73	0	\N
108	74	0	\N
109	75	0	\N
110	76	0	\N
111	77	0	\N
112	78	0	\N
113	79	0	\N
114	80	0	\N
115	81	0	\N
116	82	0	\N
117	83	0	\N
118	84	0	\N
119	85	0	\N
120	86	0	\N
121	87	0	\N
122	88	0	\N
123	89	0	\N
124	90	0	\N
125	91	0	\N
126	92	0	\N
127	93	0	\N
128	94	0	\N
129	95	0	\N
130	96	0	\N
131	97	0	\N
132	98	0	\N
133	99	0	\N
134	100	0	\N
135	101	0	\N
136	102	0	\N
137	103	0	\N
138	104	0	\N
139	105	0	\N
140	106	0	\N
141	107	0	\N
142	108	0	\N
143	109	0	\N
144	110	0	\N
145	111	0	\N
146	112	0	\N
147	113	0	\N
148	114	0	\N
149	114	1	BOSSIO
150	115	0	\N
151	116	0	\N
152	117	0	\N
153	118	0	\N
154	119	0	\N
155	120	0	\N
156	120	1	NUEVA LEHMANN
157	121	0	\N
158	122	0	\N
159	123	0	\N
160	124	0	\N
161	125	0	\N
162	126	0	\N
163	127	0	\N
164	128	0	\N
165	128	1	PUEBLO TERRAGNI
166	129	0	\N
167	129	1	EST PTE ROCA
168	130	1	SECCION A
169	130	2	SECCION B
170	130	3	SECCION C
171	130	4	SECCION D
172	131	0	\N
173	132	0	\N
174	133	0	\N
175	134	0	\N
176	135	0	\N
177	135	1	EST SAGUIER
178	136	0	\N
179	137	0	\N
180	138	0	\N
181	139	0	\N
182	140	0	\N
183	140	1	EST ESTRADA
184	141	0	\N
185	142	0	\N
186	143	0	\N
187	144	0	\N
188	145	0	\N
189	146	0	\N
190	146	1	EST KM 501
191	147	0	\N
192	147	1	EST JOSEFINA
193	148	0	\N
194	149	0	\N
195	150	0	\N
196	150	1	EST M JUANA
197	151	0	\N
198	152	0	\N
199	152	1	LOS SEMBRADOS
200	153	0	\N
201	154	0	\N
202	155	0	\N
203	156	0	\N
204	157	0	\N
205	158	0	\N
206	159	0	\N
207	160	0	\N
208	161	0	\N
209	162	0	\N
210	163	0	\N
211	164	0	\N
212	165	0	\N
213	166	0	\N
214	167	0	\N
215	168	0	\N
216	169	0	\N
217	170	0	\N
218	170	1	COLONIA NUEVA
219	171	0	\N
220	172	0	\N
221	173	0	\N
222	174	0	\N
223	175	0	\N
224	176	0	\N
225	177	0	\N
226	178	0	\N
227	179	0	\N
228	180	0	\N
229	181	0	\N
230	182	0	\N
231	183	0	\N
232	184	0	\N
233	185	0	\N
234	186	0	\N
235	187	0	\N
236	188	0	ESTAC. MATILDE
237	188	1	PLAZA MATILDE
238	189	0	\N
239	190	0	\N
240	191	0	\N
241	192	0	\N
242	193	0	\N
243	194	0	\N
244	195	0	\N
245	195	1	EST MANUCHO
246	196	0	\N
247	197	0	\N
248	197	1	VILLA LAURA
249	197	2	ISLAS
250	198	0	\N
251	198	1	ISLAS
252	198	2	ANGEL GALLARDO
253	199	0	\N
254	200	1	SECCION 1
255	200	2	SECCION 2
256	200	3	SECCION 3
257	200	4	SECCION 4A
258	200	5	SECCION 4B
259	200	6	SECCION 5
260	200	7	LA GUARDIA-COL.
261	200	8	ISLAS
262	200	9	ALTO VERDE URB.
263	201	0	\N
264	202	0	\N
265	202	1	ISLAS
266	203	0	\N
267	203	1	ISLAS
268	204	0	\N
269	204	1	ISLAS
270	205	0	\N
271	206	0	\N
272	207	0	\N
273	208	0	\N
274	208	1	RIO GRANDE
275	208	2	LA CAIMA
276	208	3	ISLAS
277	209	0	\N
278	209	1	ISLAS
279	210	0	\N
280	211	0	\N
281	212	0	\N
282	213	0	\N
283	214	0	\N
284	214	1	ISLAS
285	215	0	\N
286	215	1	ISLAS
287	216	0	\N
288	217	0	\N
289	218	0	\N
290	219	0	\N
291	219	1	PUERTO ARAGON
292	219	2	ISLAS
293	220	0	\N
294	220	1	ISLAS
295	221	0	\N
296	221	1	ISLAS
297	222	0	\N
298	222	1	ISLAS
299	223	0	\N
300	224	0	\N
301	225	0	\N
302	226	0	\N
303	227	0	\N
304	228	0	\N
305	229	0	\N
306	229	1	KM 465
307	230	0	\N
308	231	0	\N
309	231	1	WILDERMUT
310	232	0	\N
311	233	0	\N
312	234	0	\N
313	235	0	\N
314	236	0	\N
315	236	1	SCHIFFNER
316	237	0	\N
317	238	0	\N
318	239	0	\N
319	240	0	\N
320	241	0	\N
321	242	0	\N
322	243	0	\N
323	244	0	\N
324	245	0	\N
325	246	0	\N
326	247	0	\N
327	248	0	\N
328	249	0	\N
329	250	0	\N
330	251	0	\N
331	251	1	LARGUIA
332	252	0	\N
333	253	0	\N
334	253	1	LA RIBERA
335	254	0	\N
336	255	0	\N
337	256	0	\N
338	257	0	\N
339	258	0	\N
340	259	0	\N
341	259	1	SECCION 1
342	259	2	SECCION 2
343	259	3	SECCION 3
344	259	4	SECCION 4
345	260	0	\N
346	260	1	MARIA L CORREA
347	261	0	\N
348	261	1	SAN RICARDO
349	262	0	\N
350	262	1	ISLAS
351	263	0	\N
352	263	1	PUEBLO KIRTEN
353	264	0	\N
354	264	1	SECCION 1
355	264	2	SECCION 2
356	264	3	SECCION 3A
357	264	4	SECCION 3B
358	264	5	SECCION 3C
359	264	6	SECCION 4
360	264	7	SECCION 5
361	264	8	SECCION 6
362	264	9	SECCION 7
363	265	0	\N
364	266	0	\N
365	266	1	ISLAS
366	267	0	\N
367	268	0	\N
368	269	0	\N
369	270	0	\N
370	271	0	\N
371	272	0	\N
372	273	0	\N
373	274	0	\N
374	275	0	\N
375	276	0	\N
376	277	0	\N
377	278	0	\N
378	278	1	ISLAS
379	279	1	SECCION 1
380	279	2	SECCION 2
381	279	3	SECCION 3
382	279	4	SECCION 4
383	279	5	SECCION 5
384	279	6	SECCION 6
385	279	7	SECCION 7
386	279	8	SECCION 8
387	279	9	SECCION 9
388	279	10	SECCION 10
389	279	11	SECCION 11
390	279	12	SECCION 12
391	279	13	SECCION 13
392	279	14	SECCION 14
393	279	15	SECCION 15
394	279	16	SECCION 16
395	279	17	SECCION 17
396	279	18	SECCION 18
397	279	19	SECCION 19
398	279	20	SECCION 20
399	279	21	SECCION 21
400	280	0	\N
401	281	0	\N
402	282	0	\N
403	283	0	\N
404	284	0	\N
405	285	0	\N
406	286	0	\N
407	287	0	\N
408	288	0	\N
409	289	0	\N
410	290	0	\N
411	290	1	CUATRO ESQUINAS
412	291	0	\N
413	292	0	\N
414	293	0	\N
415	294	0	\N
416	294	1	ISLAS
417	295	0	\N
418	295	1	ISLAS
419	296	0	\N
420	297	0	\N
421	298	0	\N
422	299	0	\N
423	300	0	\N
424	300	1	ISLAS
425	301	0	\N
426	302	0	\N
427	303	0	\N
428	304	0	\N
429	305	0	\N
430	306	0	\N
431	306	1	V FREDRICKSON
432	307	0	\N
433	308	0	\N
434	309	0	\N
435	310	0	\N
436	311	0	\N
437	312	0	\N
438	313	0	\N
439	313	1	POLIGONO 1
440	313	2	POLIGONO 2
441	313	3	POLIGONO 3
442	313	4	POLIGONO 4
443	313	5	POLIGONO 5
444	313	6	POLIGONO 6
445	313	7	AMPLIACIONES
446	314	0	\N
447	315	0	\N
448	316	0	\N
449	317	0	\N
450	318	0	\N
451	319	0	\N
452	320	0	\N
453	321	0	\N
454	322	0	\N
455	323	0	\N
456	323	1	SAN MARCELO
457	324	0	\N
458	325	0	\N
459	325	1	CAMPANA
460	326	0	\N
461	327	0	\N
462	327	1	POLIGONO 1
463	327	2	POLIGONO 2
464	327	3	POLIGONO 3
465	327	4	POLIGONO 4
466	327	5	POLIGONO 5
467	327	6	POLIGONO 6
468	327	7	AMPLIACIONES
469	328	0	\N
470	329	0	\N
471	330	0	\N
472	331	0	\N
473	332	0	\N
474	333	0	\N
475	333	1	FENDWICK
476	334	0	\N
477	335	0	\N
478	336	0	\N
479	336	1	SECCION A
480	336	2	SECCION B
481	336	3	SECCION C
482	336	4	SECCION D
483	336	5	SECCION E
484	336	7	SECCION A N R
485	336	8	SECCION B N R
486	336	9	SECCION C N R
487	336	10	SECCION D N R
488	336	11	SECCION E N R
489	336	12	POL 3 Y 4 URB
490	337	0	\N
491	338	0	\N
492	339	0	\N
493	340	0	\N
494	341	0	\N
495	341	1	PUEBLO HANSEN
496	342	0	\N
497	343	0	\N
498	344	0	\N
499	345	0	\N
500	346	0	\N
501	347	0	\N
502	348	0	\N
503	349	0	\N
504	350	0	\N
505	351	0	\N
506	352	0	\N
507	352	1	FONTANELLA
508	353	0	\N
509	354	0	\N
510	355	0	\N
511	355	1	CAÑADA RICA
512	356	0	\N
513	357	0	\N
514	358	0	\N
515	359	0	\N
516	360	0	\N
517	361	0	\N
518	362	0	\N
519	362	1	ISLAS
520	363	0	\N
\.


--
-- Name: sd_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 
--

SELECT setval('sd_id_seq', 520, false);


--
-- Data for Name: titulo; Type: TABLE DATA; Schema: public; Owner: 
--

COPY titulo (id, nombre) FROM stdin;
1	Agrimensor
2	Agrimensor Nacional
3	Ingeniero Agrimensor
4	Ingeniero Civil
5	Ingeniero Geógrafo
\.


--
-- Name: titulo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: 
--

SELECT setval('titulo_id_seq', 5, true);


--
-- Data for Name: zona; Type: TABLE DATA; Schema: public; Owner: 
--

COPY zona (id, descripcion) FROM stdin;
1	Urbana
2	Suburbana (quintas, etc)
3	Suburbana (urbanización, loteos)
4	Parcelas Rurales (explotaciones agropecuarias)
5	Parcelas Rurales (estableciamientos industriales)
\.

