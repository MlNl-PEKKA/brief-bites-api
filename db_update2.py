import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
article = {
                    "title": "Virat Kohli Returns To Captain RCB Despite Faf du Plessis Playing. Here's Why - NDTV Sports",
                    "link": "https://news.google.com/rss/articles/CBMieGh0dHBzOi8vc3BvcnRzLm5kdHYuY29tL2lwbC0yMDIzL3ZpcmF0LWtvaGxpLXJldHVybnMtdG8tY2FwdGFpbi1yY2ItZXhwbGFpbnMtcmVhc29uLWJlaGluZC1jaGFuZ2UtZm9yLXBia3MtbWF0Y2gtMzk2NDQ4NtIBfmh0dHBzOi8vc3BvcnRzLm5kdHYuY29tL2lwbC0yMDIzL3ZpcmF0LWtvaGxpLXJldHVybnMtdG8tY2FwdGFpbi1yY2ItZXhwbGFpbnMtcmVhc29uLWJlaGluZC1jaGFuZ2UtZm9yLXBia3MtbWF0Y2gtMzk2NDQ4Ni9hbXAvMQ?oc=5",
                    "time": "Fri, 21 Apr 2023 07:14:54 GMT",
                    "source": "NDTV Sports",
                    "common_category": [
                        "sports"
                    ],
                    "text": "As the Royal Challengers Bangalore took on Punjab Kings in an Indian Premier League (IPL) 2023 match on Thursday, two stand-in skippers arrived in the form of Virat Kohli and Sam Curran. While Kohli was deputising for injured Faf du Plessis, Curran wore the captain's hat in place of Shikhar Dhawan who missed the second consecutive match for his franchise. After Curran opted to bowl first upon winning the toss, Kohli was asked the reason behind him donning the skipper's hat in place of Du Plessis.. Kohli explained that Du Plessis is carrying a rib injury because of which he wouldn't be able to field. Hence, the decision to play him as an 'Impact Player' was taken by the team management.. 'Faf potentially can't be fielding today, so he'll be playing as an impact player, switching with Vyshak. We got to do what we wanted, we would have batted first, the pitch could get slow, some scruff marks will help the bowlers going deep into the game. Taking one game at a time, focussing on our own game, make the most of crunch situations, we haven't done that so far in the tournament. No other changes for us,' Kohli revealed at the time of the toss.. Royal Challengers Bangalore Playing XI:Virat Kohli(c), Faf du Plessis, Mahipal Lomror, Glenn Maxwell, Shahbaz Ahmed, Dinesh Karthik(w), Wanindu Hasaranga, Suyash Prabhudessai, Harshal Patel, Wayne Parnell, Mohammed Siraj. While Faf will come out to bat with Kohli, it would Vijaykumar Vyshak who will be playing in his place when the substitution takes place.. Sponsored by Vuukle. PBKS stand-in skipper Curran, on the other hand, explained that Liam Livingstone is back in the playing XI for his side while Nathan Ellis has also returned, replacing Kagiso Rabada.. 'We will bowl first, did well in the last game and we'll take some confidence, conditions will not change a lot. Shikhar is getting closer, but he'll miss out today. He's a quality player, but the younger lot will have to shape up, Livingstone is back and we have Ellis back in place of KG,' he said.. Punjab Kings Playing XI:Atharva Taide, Matthew Short, Harpreet Singh Bhatia, Liam Livingstone, Sam Curran(c), Jitesh Sharma(w), Shahrukh Khan, Harpreet Brar, Nathan Ellis, Rahul Chahar, Arshdeep Singh. RCB are presently 8th in the points table while PBKS are 5th. A big win in Mohali could take the Bengaluru franchise into the top half.",
                    "klsum": {
                        "summary": "PBKS stand-in skipper Curran, on the other hand, explained that Liam Livingstone is back in the playing XI for his side while Nathan Ellis has also returned, replacing Kagiso Rabada.. 'We will bowl first, did well in the last game and we'll take some confidence, conditions will not change a lot.RCB are presently 8th in the points table while PBKS are 5th.A big win in Mohali could take the Bengaluru franchise into the top half.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    1.0,
                                    0.18944844124700239,
                                    0.3185483870967742
                                ],
                                "rouge2": [
                                    0.9871794871794872,
                                    0.18509615384615385,
                                    0.31174089068825916
                                ],
                                "rougeL": [
                                    1.0,
                                    0.18944844124700239,
                                    0.3185483870967742
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.7848101265822784,
                                    0.496,
                                    0.6078431372549019
                                ],
                                "rouge2": [
                                    0.6666666666666666,
                                    0.41935483870967744,
                                    0.5148514851485149
                                ],
                                "rougeL": [
                                    0.6708860759493671,
                                    0.424,
                                    0.5196078431372549
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.3037974683544304,
                                    0.17777777777777778,
                                    0.22429906542056074
                                ],
                                "rouge2": [
                                    0.08974358974358974,
                                    0.05223880597014925,
                                    0.0660377358490566
                                ],
                                "rougeL": [
                                    0.12658227848101267,
                                    0.07407407407407407,
                                    0.09345794392523366
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.759493670886076,
                                    0.3821656050955414,
                                    0.5084745762711865
                                ],
                                "rouge2": [
                                    0.6666666666666666,
                                    0.3333333333333333,
                                    0.4444444444444444
                                ],
                                "rougeL": [
                                    0.6962025316455697,
                                    0.3503184713375796,
                                    0.4661016949152542
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.2911392405063291,
                                    0.46,
                                    0.3565891472868218
                                ],
                                "rouge2": [
                                    0.19230769230769232,
                                    0.30612244897959184,
                                    0.2362204724409449
                                ],
                                "rougeL": [
                                    0.25316455696202533,
                                    0.4,
                                    0.31007751937984496
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.0759493670886076,
                                    0.15789473684210525,
                                    0.10256410256410256
                                ],
                                "rouge2": [
                                    0.0,
                                    0.0,
                                    0.0
                                ],
                                "rougeL": [
                                    0.06329113924050633,
                                    0.13157894736842105,
                                    0.08547008547008547
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.3924050632911392,
                                    0.34831460674157305,
                                    0.369047619047619
                                ],
                                "rouge2": [
                                    0.08974358974358974,
                                    0.07954545454545454,
                                    0.08433734939759037
                                ],
                                "rougeL": [
                                    0.21518987341772153,
                                    0.19101123595505617,
                                    0.20238095238095238
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.3162792216272692,
                            "vklsum": 1.0,
                            "vlexrank": 0.5474341551802239,
                            "vlsa": 0.127931581731617,
                            "vluhn": 0.47300690521029504,
                            "vbart": 0.3009623797025372,
                            "vpegasus": 0.06267806267806268,
                            "vchatGPT": 0.21858864027538724
                        },
                        "final_score": 0.44772889727460846
                    },
                    "lexrank": {
                        "summary": "After Curran opted to bowl first upon winning the toss, Kohli was asked the reason behind him donning the skipper's hat in place of Du Plessis.. Kohli explained that Du Plessis is carrying a rib injury because of which he wouldn't be able to field.While Faf will come out to bat with Kohli, it would Vijaykumar Vyshak who will be playing in his place when the substitution takes place..PBKS stand-in skipper Curran, on the other hand, explained that Liam Livingstone is back in the playing XI for his side while Nathan Ellis has also returned, replacing Kagiso Rabada.. 'We will bowl first, did well in the last game and we'll take some confidence, conditions will not change a lot.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    1.0,
                                    0.2997601918465228,
                                    0.46125461254612554
                                ],
                                "rouge2": [
                                    0.9838709677419355,
                                    0.2932692307692308,
                                    0.45185185185185184
                                ],
                                "rougeL": [
                                    1.0,
                                    0.2997601918465228,
                                    0.46125461254612554
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.496,
                                    0.7848101265822784,
                                    0.6078431372549019
                                ],
                                "rouge2": [
                                    0.41935483870967744,
                                    0.6666666666666666,
                                    0.5148514851485149
                                ],
                                "rougeL": [
                                    0.424,
                                    0.6708860759493671,
                                    0.5196078431372549
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.368,
                                    0.34074074074074073,
                                    0.35384615384615387
                                ],
                                "rouge2": [
                                    0.10483870967741936,
                                    0.09701492537313433,
                                    0.1007751937984496
                                ],
                                "rougeL": [
                                    0.152,
                                    0.14074074074074075,
                                    0.14615384615384616
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.848,
                                    0.6751592356687898,
                                    0.75177304964539
                                ],
                                "rouge2": [
                                    0.7903225806451613,
                                    0.6282051282051282,
                                    0.7000000000000001
                                ],
                                "rougeL": [
                                    0.8,
                                    0.6369426751592356,
                                    0.7092198581560283
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.248,
                                    0.62,
                                    0.3542857142857143
                                ],
                                "rouge2": [
                                    0.1532258064516129,
                                    0.3877551020408163,
                                    0.21965317919075145
                                ],
                                "rougeL": [
                                    0.2,
                                    0.5,
                                    0.28571428571428575
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.12,
                                    0.39473684210526316,
                                    0.18404907975460122
                                ],
                                "rouge2": [
                                    0.04838709677419355,
                                    0.16216216216216217,
                                    0.07453416149068322
                                ],
                                "rougeL": [
                                    0.064,
                                    0.21052631578947367,
                                    0.09815950920245399
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.36,
                                    0.5056179775280899,
                                    0.4205607476635514
                                ],
                                "rouge2": [
                                    0.10483870967741936,
                                    0.14772727272727273,
                                    0.12264150943396228
                                ],
                                "rougeL": [
                                    0.16,
                                    0.2247191011235955,
                                    0.18691588785046728
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.45812035898136766,
                            "vklsum": 0.5474341551802239,
                            "vlexrank": 1.0,
                            "vlsa": 0.20025839793281655,
                            "vluhn": 0.7203309692671395,
                            "vbart": 0.2865510597302505,
                            "vpegasus": 0.11891425014924613,
                            "vchatGPT": 0.24337271498266033
                        },
                        "final_score": 0.5063375621828807
                    },
                    "lsa": {
                        "summary": "Hence, the decision to play him as an 'Impact Player' was taken by the team management.. 'Faf potentially can't be fielding today, so he'll be playing as an impact player, switching with Vyshak.No other changes for us,' Kohli revealed at the time of the toss.. Royal Challengers Bangalore Playing XI:Virat Kohli(c), Faf du Plessis, Mahipal Lomror, Glenn Maxwell, Shahbaz Ahmed, Dinesh Karthik(w), Wanindu Hasaranga, Suyash Prabhudessai, Harshal Patel, Wayne Parnell, Mohammed Siraj.He's a quality player, but the younger lot will have to shape up, Livingstone is back and we have Ellis back in place of KG,' he said.. Punjab Kings Playing XI:Atharva Taide, Matthew Short, Harpreet Singh Bhatia, Liam Livingstone, Sam Curran(c), Jitesh Sharma(w), Shahrukh Khan, Harpreet Brar, Nathan Ellis, Rahul Chahar, Arshdeep Singh.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    1.0,
                                    0.3237410071942446,
                                    0.4891304347826087
                                ],
                                "rouge2": [
                                    0.9850746268656716,
                                    0.3173076923076923,
                                    0.4799999999999999
                                ],
                                "rougeL": [
                                    1.0,
                                    0.3237410071942446,
                                    0.4891304347826087
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.17777777777777778,
                                    0.3037974683544304,
                                    0.22429906542056074
                                ],
                                "rouge2": [
                                    0.05223880597014925,
                                    0.08974358974358974,
                                    0.0660377358490566
                                ],
                                "rougeL": [
                                    0.07407407407407407,
                                    0.12658227848101267,
                                    0.09345794392523366
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.34074074074074073,
                                    0.368,
                                    0.35384615384615387
                                ],
                                "rouge2": [
                                    0.09701492537313433,
                                    0.10483870967741936,
                                    0.1007751937984496
                                ],
                                "rougeL": [
                                    0.14074074074074075,
                                    0.152,
                                    0.14615384615384616
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.5925925925925926,
                                    0.5095541401273885,
                                    0.547945205479452
                                ],
                                "rouge2": [
                                    0.44776119402985076,
                                    0.38461538461538464,
                                    0.41379310344827586
                                ],
                                "rougeL": [
                                    0.4962962962962963,
                                    0.4267515923566879,
                                    0.45890410958904104
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.21481481481481482,
                                    0.58,
                                    0.31351351351351353
                                ],
                                "rouge2": [
                                    0.11940298507462686,
                                    0.32653061224489793,
                                    0.17486338797814205
                                ],
                                "rougeL": [
                                    0.13333333333333333,
                                    0.36,
                                    0.1945945945945946
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.14814814814814814,
                                    0.5263157894736842,
                                    0.23121387283236994
                                ],
                                "rouge2": [
                                    0.06716417910447761,
                                    0.24324324324324326,
                                    0.10526315789473684
                                ],
                                "rougeL": [
                                    0.08888888888888889,
                                    0.3157894736842105,
                                    0.13872832369942198
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.28888888888888886,
                                    0.43820224719101125,
                                    0.3482142857142857
                                ],
                                "rouge2": [
                                    0.1044776119402985,
                                    0.1590909090909091,
                                    0.12612612612612614
                                ],
                                "rougeL": [
                                    0.11851851851851852,
                                    0.1797752808988764,
                                    0.14285714285714285
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.4860869565217391,
                            "vklsum": 0.127931581731617,
                            "vlexrank": 0.20025839793281655,
                            "vlsa": 1.0,
                            "vluhn": 0.4735474728389229,
                            "vbart": 0.22765716536208339,
                            "vpegasus": 0.15840178480884293,
                            "vchatGPT": 0.20573251823251826
                        },
                        "final_score": 0.41689033261171354
                    },
                    "luhn": {
                        "summary": "After Curran opted to bowl first upon winning the toss, Kohli was asked the reason behind him donning the skipper's hat in place of Du Plessis.. Kohli explained that Du Plessis is carrying a rib injury because of which he wouldn't be able to field.PBKS stand-in skipper Curran, on the other hand, explained that Liam Livingstone is back in the playing XI for his side while Nathan Ellis has also returned, replacing Kagiso Rabada.. 'We will bowl first, did well in the last game and we'll take some confidence, conditions will not change a lot.He's a quality player, but the younger lot will have to shape up, Livingstone is back and we have Ellis back in place of KG,' he said.. Punjab Kings Playing XI:Atharva Taide, Matthew Short, Harpreet Singh Bhatia, Liam Livingstone, Sam Curran(c), Jitesh Sharma(w), Shahrukh Khan, Harpreet Brar, Nathan Ellis, Rahul Chahar, Arshdeep Singh.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    1.0,
                                    0.3764988009592326,
                                    0.5470383275261325
                                ],
                                "rouge2": [
                                    0.9871794871794872,
                                    0.3701923076923077,
                                    0.5384615384615385
                                ],
                                "rougeL": [
                                    1.0,
                                    0.3764988009592326,
                                    0.5470383275261325
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.3821656050955414,
                                    0.759493670886076,
                                    0.5084745762711865
                                ],
                                "rouge2": [
                                    0.3333333333333333,
                                    0.6666666666666666,
                                    0.4444444444444444
                                ],
                                "rougeL": [
                                    0.3503184713375796,
                                    0.6962025316455697,
                                    0.4661016949152542
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.6751592356687898,
                                    0.848,
                                    0.75177304964539
                                ],
                                "rouge2": [
                                    0.6282051282051282,
                                    0.7903225806451613,
                                    0.7000000000000001
                                ],
                                "rougeL": [
                                    0.6369426751592356,
                                    0.8,
                                    0.7092198581560283
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.5095541401273885,
                                    0.5925925925925926,
                                    0.547945205479452
                                ],
                                "rouge2": [
                                    0.38461538461538464,
                                    0.44776119402985076,
                                    0.41379310344827586
                                ],
                                "rougeL": [
                                    0.4267515923566879,
                                    0.4962962962962963,
                                    0.45890410958904104
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.20382165605095542,
                                    0.64,
                                    0.30917874396135264
                                ],
                                "rouge2": [
                                    0.1282051282051282,
                                    0.40816326530612246,
                                    0.19512195121951217
                                ],
                                "rougeL": [
                                    0.1592356687898089,
                                    0.5,
                                    0.24154589371980675
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.10828025477707007,
                                    0.4473684210526316,
                                    0.17435897435897435
                                ],
                                "rouge2": [
                                    0.05128205128205128,
                                    0.21621621621621623,
                                    0.08290155440414508
                                ],
                                "rougeL": [
                                    0.06369426751592357,
                                    0.2631578947368421,
                                    0.10256410256410257
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.28662420382165604,
                                    0.5056179775280899,
                                    0.36585365853658536
                                ],
                                "rouge2": [
                                    0.09615384615384616,
                                    0.17045454545454544,
                                    0.12295081967213115
                                ],
                                "rougeL": [
                                    0.1337579617834395,
                                    0.23595505617977527,
                                    0.17073170731707316
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.5441793978379345,
                            "vklsum": 0.47300690521029504,
                            "vlexrank": 0.7203309692671395,
                            "vlsa": 0.4735474728389229,
                            "vluhn": 1.0,
                            "vbart": 0.24861552963355718,
                            "vpegasus": 0.11994154377574068,
                            "vchatGPT": 0.21984539517526325
                        },
                        "final_score": 0.5020495221654603
                    },
                    "bart": {
                        "summary": "Royal Challengers Bangalore took on Punjab Kings in an IPL2023 match on Thursday. Virat Kohli was playing as captain in place of the injured Faf du Plessis. Shikhar Dhawan missed the match. Liam Livingstone is back in the playing XI for PBKS. Nathan Ellis has also returned, replacing Kagiso Rabada.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    0.98,
                                    0.11750599520383694,
                                    0.2098501070663812
                                ],
                                "rouge2": [
                                    0.7346938775510204,
                                    0.08653846153846154,
                                    0.15483870967741933
                                ],
                                "rougeL": [
                                    0.82,
                                    0.09832134292565947,
                                    0.17558886509635974
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.46,
                                    0.2911392405063291,
                                    0.3565891472868218
                                ],
                                "rouge2": [
                                    0.30612244897959184,
                                    0.19230769230769232,
                                    0.2362204724409449
                                ],
                                "rougeL": [
                                    0.4,
                                    0.25316455696202533,
                                    0.31007751937984496
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.62,
                                    0.248,
                                    0.3542857142857143
                                ],
                                "rouge2": [
                                    0.3877551020408163,
                                    0.1532258064516129,
                                    0.21965317919075145
                                ],
                                "rougeL": [
                                    0.5,
                                    0.2,
                                    0.28571428571428575
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.58,
                                    0.21481481481481482,
                                    0.31351351351351353
                                ],
                                "rouge2": [
                                    0.32653061224489793,
                                    0.11940298507462686,
                                    0.17486338797814205
                                ],
                                "rougeL": [
                                    0.36,
                                    0.13333333333333333,
                                    0.1945945945945946
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.64,
                                    0.20382165605095542,
                                    0.30917874396135264
                                ],
                                "rouge2": [
                                    0.40816326530612246,
                                    0.1282051282051282,
                                    0.19512195121951217
                                ],
                                "rougeL": [
                                    0.5,
                                    0.1592356687898089,
                                    0.24154589371980675
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.54,
                                    0.7105263157894737,
                                    0.6136363636363636
                                ],
                                "rouge2": [
                                    0.3877551020408163,
                                    0.5135135135135135,
                                    0.441860465116279
                                ],
                                "rougeL": [
                                    0.42,
                                    0.5526315789473685,
                                    0.4772727272727273
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.74,
                                    0.4157303370786517,
                                    0.5323741007194244
                                ],
                                "rouge2": [
                                    0.3673469387755102,
                                    0.20454545454545456,
                                    0.26277372262773724
                                ],
                                "rougeL": [
                                    0.48,
                                    0.2696629213483146,
                                    0.3453237410071942
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.18009256061338674,
                            "vklsum": 0.3009623797025372,
                            "vlexrank": 0.2865510597302505,
                            "vlsa": 0.22765716536208339,
                            "vluhn": 0.24861552963355718,
                            "vbart": 1.0,
                            "vpegasus": 0.51092318534179,
                            "vchatGPT": 0.38015718811811866
                        },
                        "final_score": 0.8628107628268064
                    },
                    "pegasus": {
                        "summary": "Royal Challengers Bangalore took on Punjab Kings in an Indian Premier League (IPL) 2023 match on Thursday .Virat Kohli was deputising for injured Faf du Plessis .Sam Curran wore the captain's hat in place of Shikhar Dhawan .",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    1.0,
                                    0.09112709832134293,
                                    0.16703296703296702
                                ],
                                "rouge2": [
                                    0.9459459459459459,
                                    0.08413461538461539,
                                    0.1545253863134658
                                ],
                                "rougeL": [
                                    0.9736842105263158,
                                    0.08872901678657075,
                                    0.16263736263736264
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.15789473684210525,
                                    0.0759493670886076,
                                    0.10256410256410256
                                ],
                                "rouge2": [
                                    0.0,
                                    0.0,
                                    0.0
                                ],
                                "rougeL": [
                                    0.13157894736842105,
                                    0.06329113924050633,
                                    0.08547008547008547
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.39473684210526316,
                                    0.12,
                                    0.18404907975460122
                                ],
                                "rouge2": [
                                    0.16216216216216217,
                                    0.04838709677419355,
                                    0.07453416149068322
                                ],
                                "rougeL": [
                                    0.21052631578947367,
                                    0.064,
                                    0.09815950920245399
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.5263157894736842,
                                    0.14814814814814814,
                                    0.23121387283236994
                                ],
                                "rouge2": [
                                    0.24324324324324326,
                                    0.06716417910447761,
                                    0.10526315789473684
                                ],
                                "rougeL": [
                                    0.3157894736842105,
                                    0.08888888888888889,
                                    0.13872832369942198
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.4473684210526316,
                                    0.10828025477707007,
                                    0.17435897435897435
                                ],
                                "rouge2": [
                                    0.21621621621621623,
                                    0.05128205128205128,
                                    0.08290155440414508
                                ],
                                "rougeL": [
                                    0.2631578947368421,
                                    0.06369426751592357,
                                    0.10256410256410257
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.7105263157894737,
                                    0.54,
                                    0.6136363636363636
                                ],
                                "rouge2": [
                                    0.5135135135135135,
                                    0.3877551020408163,
                                    0.441860465116279
                                ],
                                "rougeL": [
                                    0.5526315789473685,
                                    0.42,
                                    0.4772727272727273
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    0.7368421052631579,
                                    0.3146067415730337,
                                    0.4409448818897637
                                ],
                                "rouge2": [
                                    0.40540540540540543,
                                    0.17045454545454544,
                                    0.23999999999999996
                                ],
                                "rougeL": [
                                    0.6052631578947368,
                                    0.25842696629213485,
                                    0.3622047244094488
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.16139857199459848,
                            "vklsum": 0.06267806267806268,
                            "vlexrank": 0.11891425014924613,
                            "vlsa": 0.15840178480884293,
                            "vluhn": 0.11994154377574068,
                            "vbart": 0.51092318534179,
                            "vpegasus": 1.0,
                            "vchatGPT": 0.34771653543307085
                        },
                        "final_score": 0.7894494524511336
                    },
                    "chatGPT": {
                        "summary": "Royal Challengers Bangalore took on Punjab Kings in an IPL match with stand-in captains Virat Kohli and Sam Curran. Kohli explained that he was deputizing for injured Faf du Plessis, who would play as an \"Impact Player\" due to a rib injury. RCB opted to field first on winning the toss. Punjab Kings brought in Liam Livingstone and Nathan Ellis, while Shikhar Dhawan missed out for the second consecutive match. Both teams needed a win, with RCB in 8th place and PBKS in 5th in the points table.",
                        "rouge": {
                            "vtext": {
                                "rouge1": [
                                    0.9325842696629213,
                                    0.19904076738609114,
                                    0.3280632411067194
                                ],
                                "rouge2": [
                                    0.45454545454545453,
                                    0.09615384615384616,
                                    0.15873015873015872
                                ],
                                "rougeL": [
                                    0.5730337078651685,
                                    0.1223021582733813,
                                    0.2015810276679842
                                ]
                            },
                            "vklsum": {
                                "rouge1": [
                                    0.34831460674157305,
                                    0.3924050632911392,
                                    0.369047619047619
                                ],
                                "rouge2": [
                                    0.07954545454545454,
                                    0.08974358974358974,
                                    0.08433734939759037
                                ],
                                "rougeL": [
                                    0.19101123595505617,
                                    0.21518987341772153,
                                    0.20238095238095238
                                ]
                            },
                            "vlexrank": {
                                "rouge1": [
                                    0.5056179775280899,
                                    0.36,
                                    0.4205607476635514
                                ],
                                "rouge2": [
                                    0.14772727272727273,
                                    0.10483870967741936,
                                    0.12264150943396228
                                ],
                                "rougeL": [
                                    0.2247191011235955,
                                    0.16,
                                    0.18691588785046728
                                ]
                            },
                            "vlsa": {
                                "rouge1": [
                                    0.43820224719101125,
                                    0.28888888888888886,
                                    0.3482142857142857
                                ],
                                "rouge2": [
                                    0.1590909090909091,
                                    0.1044776119402985,
                                    0.12612612612612614
                                ],
                                "rougeL": [
                                    0.1797752808988764,
                                    0.11851851851851852,
                                    0.14285714285714285
                                ]
                            },
                            "vluhn": {
                                "rouge1": [
                                    0.5056179775280899,
                                    0.28662420382165604,
                                    0.36585365853658536
                                ],
                                "rouge2": [
                                    0.17045454545454544,
                                    0.09615384615384616,
                                    0.12295081967213115
                                ],
                                "rougeL": [
                                    0.23595505617977527,
                                    0.1337579617834395,
                                    0.17073170731707316
                                ]
                            },
                            "vbart": {
                                "rouge1": [
                                    0.4157303370786517,
                                    0.74,
                                    0.5323741007194244
                                ],
                                "rouge2": [
                                    0.20454545454545456,
                                    0.3673469387755102,
                                    0.26277372262773724
                                ],
                                "rougeL": [
                                    0.2696629213483146,
                                    0.48,
                                    0.3453237410071942
                                ]
                            },
                            "vpegasus": {
                                "rouge1": [
                                    0.3146067415730337,
                                    0.7368421052631579,
                                    0.4409448818897637
                                ],
                                "rouge2": [
                                    0.17045454545454544,
                                    0.40540540540540543,
                                    0.23999999999999996
                                ],
                                "rougeL": [
                                    0.25842696629213485,
                                    0.6052631578947368,
                                    0.3622047244094488
                                ]
                            },
                            "vchatGPT": {
                                "rouge1": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rouge2": [
                                    1.0,
                                    1.0,
                                    1.0
                                ],
                                "rougeL": [
                                    1.0,
                                    1.0,
                                    1.0
                                ]
                            }
                        },
                        "score": {
                            "vtext": 0.22945814250162078,
                            "vklsum": 0.21858864027538724,
                            "vlexrank": 0.24337271498266033,
                            "vlsa": 0.20573251823251826,
                            "vluhn": 0.21984539517526325,
                            "vbart": 0.38015718811811866,
                            "vpegasus": 0.34771653543307085,
                            "vchatGPT": 1.0
                        },
                        "final_score": 0.7799034162870587
                    },
                    "id": "7859e05f9aac4178fb8605ed0d8567c6246c9ec4",
                    "votes": 0,
                    "imgUrl": "https://c.ndtvimg.com/2023-04/oo0m09jg_virat-kohli-captain-bcci_625x300_20_April_23.jpg?im=FitAndFill,algorithm=dnn,width=1200,height=675"
                }
db.collection('community').document(article['id']).set(article)
print('🔥')