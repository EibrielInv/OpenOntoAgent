sentences = [
    {
        'OriginalSentence': 'Shehan told him about the layoffs.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 1,
        'min-maxScores': [22.0, 22.0],
        'results': [
            {
                'TMR': {
                    'DESCRIBE-1': {
                        'AGENT': 'HUMAN-1',
                        'PART-OF-EVENT': 'INFORM-1',
                        'THEME': 'DISMISS-1',
                        'concept': 'DESCRIBE',
                        'from-refsem': 'REFSEM1',
                        'from-sense': 'TELL-V13',
                        'sem-preference': 4,
                        'sent-word-ind': [1, [1]],
                        'token': 'told'
                    },
                    'DISMISS-1': {
                        'CARDINALITY': ['>', 1],
                        'THEME-OF': 'INFORM-1',
                        'THEME-OF-1': 'DESCRIBE-1',
                        'concept': 'DISMISS',
                        'from-sense': 'LAYOFF-N1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [1, [5]],
                        'token': 'layoffs'
                    },
                    'HUMAN-1': {
                        'AGENT-OF': 'INFORM-1',
                        'AGENT-OF-1': 'DESCRIBE-1',
                        'HAS-PERSONAL-NAME': 'SHEHAN',
                        'concept': 'HUMAN',
                        'from-sense': 'PERSON-NAME',
                        'is-in-subtree': 'OBJECT',
                        'lex-source': 'NER',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [1, [0]],
                        'token': 'Shehan'
                    },
                    'HUMAN-2': {
                        'BENEFICIARY-OF': 'INFORM-1',
                        'GENDER': 'MALE',
                        'concept': 'HUMAN',
                        'coref': [],
                        'from-sense': 'HE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [1, [2]],
                        'token': 'him'
                    },
                    'INFORM-1': {
                        'AGENT': 'HUMAN-1',
                        'BENEFICIARY': 'HUMAN-2',
                        'HAS-EVENT-AS-PART': 'DESCRIBE-1',
                        'THEME': 'DISMISS-1',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'INFORM',
                        'from-sense': 'TELL-V13',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 6,
                        'sent-word-ind': [1, [1]],
                        'token': 'told'
                    },
                    'baseline-semantic-score': 5,
                    'combined-score': 22.0,
                    'semantic-score': 10,
                    'syntactic-score': 20.0
                },
            }
        ],
        'sent-num': 1,
        'sentence': 'Shehan told him about the layoffs.',
        'timestamp': '2020-Mar-22 21:18:38'
    },

    {
        'OriginalSentence': 'Dawami says neighbors told her they heard Hassan beat the girl.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 4,
        'min-maxScores': [40.4, 41.8],
        'results': [
            {
                'TMR': {
                    'ASPECT-3': {
                        'ITERATION': 'MULTIPLE',
                        'SCOPE': 'HIT-3',
                        'concept': 'ASPECT',
                        'from-sense': 'BEAT-V1',
                        'sem-preference': 0,
                        'sent-word-ind': [2, [8]],
                        'token': 'beat'
                    },

                    'ASSERTIVE-ACT-3': {
                        'AGENT': 'HUMAN-3',
                        'THEME': 'INFORM-3',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'ASSERTIVE-ACT',
                        'from-sense': 'SAY-V2',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [2, [1]],
                        'token': 'says'
                    },

                    'HIT-3': {
                        'AGENT': 'HUMAN-5',
                        'SCOPE-OF': 'MODALITY-3',
                        'SCOPE-OF-1': 'ASPECT-3',
                        'THEME': 'HUMAN-6',
                        'THEME-OF': 'SPEECH-ACT-3',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'HIT',
                        'from-sense': 'BEAT-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [2, [8]],
                        'token': 'beat'
                    },

                    'HUMAN-3': {
                        'AGENT-OF': 'ASSERTIVE-ACT-3',
                        'HAS-PERSONAL-NAME': 'DAWAMI',
                        'concept': 'HUMAN',
                        'from-sense': 'PERSON-NAME',
                        'is-in-subtree': 'OBJECT',
                        'lex-source': 'NER',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [0]],
                        'token': 'Dawami'
                    },

                    'HUMAN-4': {
                        'BENEFICIARY-OF': 'INFORM-3',
                        'GENDER': 'FEMALE',
                        'concept': 'HUMAN',
                        'coref': [],
                        'from-sense': 'SHE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [4]],
                        'token': 'her'
                    },

                    'HUMAN-5': {
                        'AGENT-OF': 'HIT-3',
                        'GENDER': 'MALE',
                        'HAS-PERSONAL-NAME': 'HASSAN',
                        'concept': 'HUMAN',
                        'from-sense': 'PERSON-NAME',
                        'is-in-subtree': 'OBJECT',
                        'lex-source': 'NER',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [7]],
                        'token': 'Hassan'
                    },

                    'HUMAN-6': {
                        'GENDER': 'FEMALE',
                        'THEME-OF': 'HIT-3',
                        'concept': 'HUMAN',
                        'from-sense': 'GIRL-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [10]],
                        'token': 'girl'
                    },

                    'INFORM-3': {
                        'AGENT': 'NEIGHBOR-3',
                        'BENEFICIARY': 'HUMAN-4',
                        'THEME': 'SPEECH-ACT-3',
                        'THEME-OF': 'ASSERTIVE-ACT-3',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'INFORM',
                        'from-sense': 'TELL-V2',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 6,
                        'sent-word-ind': [2, [3]],
                        'token': 'told'
                    },

                    'MODALITY-3': {
                        'SCOPE': 'HIT-3',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'TYPE': 'EPISTEMIC',
                        'VALUE': 0.5,
                        'concept': 'MODALITY',
                        'from-sense': 'HEAR-V5',
                        'sem-preference': 0,
                        'sent-word-ind': [2, [6]],
                        'token': 'heard'
                    },

                    'NEIGHBOR-3': {
                        'AGENT-OF': 'INFORM-3',
                        'CARDINALITY': ['>', 1],
                        'concept': 'NEIGHBOR',
                        'from-sense': 'NEIGHBOR-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [2]],
                        'token': 'neighbors'
                    },

                    'SET-3': {
                        'BENEFICIARY-OF': 'SPEECH-ACT-3',
                        'CARDINALITY': ['>', 1],
                        'MEMBER-TYPE': 'ALL',
                        'concept': 'SET',
                        'coref': [],
                        'from-sense': 'THEY-N1',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [2, [5]],
                        'token': 'they'
                    },

                    'SPEECH-ACT-3': {
                        'BENEFICIARY': 'SET-3',
                        'THEME': 'HIT-3',
                        'THEME-OF': 'INFORM-3',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'SPEECH-ACT',
                        'from-sense': 'HEAR-V5',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [2, [6]],
                        'token': 'heard'
                    },

                    'baseline-semantic-score': 10,
                    'combined-score': 41.8,
                    'semantic-score': 18,
                    'syntactic-score': 40.0
                },

                'concept_counts': {
                    'ASPECT': {
                        'count': 3,
                        'word-info': [[8, 'top']]
                    },
                    'ASSERTIVE-ACT': {
                        'count': 3,
                        'word-info': [[1, 'top']]
                    },
                    'HIT': {
                        'count': 3,
                        'word-info': [[8, 'top']]
                    },
                    'HUMAN': {
                        'count': 6, 'word-info': [[0, 'top'], [4, 'top'], [7, 'top'], [10, 'top']]
                    },
                    'INFORM': {
                        'count': 3, 'word-info': [[3, 'top']]
                    },
                    'MODALITY': {
                        'count': 3, 'word-info': [[6, 'top']]
                    },
                    'NEIGHBOR': {
                        'count': 3, 'word-info': [[2, 'top']]
                    },
                    'SET': {
                        'count': 3, 'word-info': [[5, 'top']]
                    },
                    'SPEECH-ACT': {
                        'count': 3, 'word-info': [[6, 'top']]}
                    },
                    'words': {
                        0: ['DAWAMI', 'PERSON-NAME', '$VAR0=0', 1],
                        1: ['SAY', 'SAY-V2', '$VAR0=1,$VAR1=0,$VAR2=3,$VAR3=None,$VAR4=None', 1],
                        2: ['NEIGHBOR', 'NEIGHBOR-N1', '$VAR0=2', 1],
                        3: ['TELL', 'TELL-V2', '$VAR0=3,$VAR1=2,$VAR2=6,$VAR3=4', 1],
                        4: ['SHE', 'SHE-N1', '$VAR0=4', 1],
                        5: ['THEY', 'THEY-N1', '$VAR0=5', 1],
                        6: ['HEAR', 'HEAR-V5', '$VAR0=6,$VAR1=5,$VAR2=8', 1],
                        7: ['HASSAN', 'PERSON-NAME', '$VAR0=7', 1],
                        8: ['BEAT', 'BEAT-V1', '$VAR0=8,$VAR1=7,$VAR2=10,$VAR3=None,$VAR4=None', 1],
                        10: ['GIRL', 'GIRL-N1', '$VAR0=10', 1],
                        11: ['.', '.-PUNCT1', '$VAR0=11', 1]
                    }
                }
            ],
            'sent-num': 2,
            'sentence': 'Dawami says neighbors told her they heard Hassan beatthe girl.',
            'timestamp': '2020-Mar-22 21:18:38'
        },

        {
            'OriginalSentence': 'I told him I hope he wins.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 2,
            'min-maxScores': [29.5, 30.0],
            'results': [
                {
                    'TMR': {
                        'HUMAN-10': {
                            'AGENT-OF': 'WIN-7',
                            'GENDER': 'MALE',
                            'concept': 'HUMAN',
                            'coref': [],
                            'from-sense': 'HE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [3, [5]],
                            'token': 'he'
                        },

                        'HUMAN-7': {
                            'AGENT-OF': 'INFORM-7',
                            'concept': 'HUMAN',
                            'from-sense': 'I-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [3, [0]],
                            'token': 'I'
                        },

                        'HUMAN-8': {
                            'BENEFICIARY-OF': 'INFORM-7',
                            'GENDER': 'MALE',
                            'concept': 'HUMAN',
                            'from-sense': 'HE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [3, [2]],
                            'token': 'him'
                        },

                        'HUMAN-9': {
                            'ATTRIBUTION': 'MODALITY-7',
                            'concept': 'HUMAN',
                            'coref': [],
                            'from-sense': 'I-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [3, [3]],
                            'token': 'I'
                        },

                        'INFORM-7': {
                            'AGENT': 'HUMAN-7',
                            'BENEFICIARY': 'HUMAN-8',
                            'THEME': 'MODALITY-7',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'INFORM',
                            'from-sense': 'TELL-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 6,
                            'sent-word-ind': [3, [1]],
                            'token': 'told'
                        },

                        'MODALITY-7': {
                            'ATTRIBUTED-TO': 'HUMAN-9',
                            'SCOPE': 'WIN-7',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'TYPE': 'VOLITIVE',
                            'VALUE': 1,
                            'concept': 'MODALITY',
                            'from-sense': 'HOPE-V1',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [3, [4]],
                            'token': 'hope'
                        },

                        'WIN-7': {
                            'AGENT': 'HUMAN-10',
                            'SCOPE-OF': 'MODALITY-7',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'WIN',
                            'from-sense': 'WIN-V1',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [3, [6]],
                            'token': 'wins'
                        },

                        'baseline-semantic-score': 5,
                        'combined-score': 30.0,
                        'semantic-score': 10,
                        'syntactic-score': 28.0},
                        'concept_counts': {
                            'HUMAN': {
                                'count': 10,
                                'word-info': [[0, 'top'], [2, 'top'], [3, 'top'], [5, 'top']]
                            },
                            'INFORM': {
                                'count': 7,
                                'word-info': [[1, 'top']]
                            },
                            'MODALITY': {
                                'count': 7, 'word-info': [[4, 'top']]
                            },
                            'WIN': {
                                'count': 7,
                                'word-info': [[6, 'top']]
                            }
                        },
                        'words': {
                            0: ['I', 'I-N1', '$VAR0=0', 1],
                            1: ['TELL', 'TELL-V2', '$VAR0=1,$VAR1=0,$VAR2=4,$VAR3=2', 1],
                            2: ['HE', 'HE-N1', '$VAR0=2', 1],
                            3: ['I', 'I-N1', '$VAR0=3', 1],
                            4: ['HOPE', 'HOPE-V1', '$VAR0=4,$VAR1=3,$VAR2=6', 1],
                            5: ['HE', 'HE-N1', '$VAR0=5', 1],
                            6: ['WIN', 'WIN-V1', '$VAR0=6,$VAR1=5,$VAR2=None', 1],
                            7: ['.', '.-PUNCT1', '$VAR0=7', 1]
                        }
                    }
                ],
                'sent-num': 3,
                'sentence': 'I told him I hope he wins.',
                'timestamp': '2020-Mar-22 21:18:38'
            },

            {
                'OriginalSentence': 'Monks teach you about Buddhism.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 1,
                'min-maxScores': [22.0, 22.0],
                'results': [
                {
                    'TMR': {
                        'BUDDHISM-11': {
                            'TOPIC-OF': 'INFORMATION-11',
                            'concept': 'BUDDHISM',
                            'from-sense': 'BUDDHISM-N2',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [4, [4]],
                            'token': 'Buddhism'
                        },

                        'HUMAN-11': {
                            'BENEFICIARY-OF': 'TEACH-11',
                            'concept': 'HUMAN',
                            'from-sense': 'YOU-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [4, [2]],
                            'token': 'you'
                        },

                        'INFORMATION-11': {
                            'ABOUT-AS-TOPIC':
                            'BUDDHISM-11',
                            'THEME-OF': 'TEACH-11',
                            'concept': 'INFORMATION',
                            'from-refsem': 'REFSEM1',
                            'from-sense': 'TEACH-V3',
                            'sem-preference': 2,
                            'sent-word-ind': [4, [1]],
                            'token': 'teach'
                        },

                        'MONK-11': {
                            'AGENT-OF': 'TEACH-11',
                            'CARDINALITY': ['>', 1],
                            'concept': 'MONK',
                            'from-sense': 'MONK-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [4, [0]],
                            'token': 'Monks'
                        },

                        'TEACH-11': {
                            'AGENT': 'MONK-11',
                            'BENEFICIARY': 'HUMAN-11',
                            'THEME': 'INFORMATION-11',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'TEACH',
                            'from-sense': 'TEACH-V3',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 4,
                            'sent-word-ind': [4, [1]],
                            'token': 'teach'
                        },

                    'baseline-semantic-score': 3,
                    'combined-score': 22.0,
                    'semantic-score': 6,
                    'syntactic-score': 20.0},
                    'concept_counts': {
                        'BUDDHISM': {
                            'count': 11,
                            'word-info': [[4, 'top']]
                        },
                        'HUMAN': {
                            'count': 11,
                            'word-info': [[2, 'top']]
                        },
                        'INFORMATION': {
                            'count': 11,
                            'word-info': [[1001, 'top']]
                        },
                        'MONK': {
                            'count': 11,
                            'word-info': [[0, 'top']]
                        },
                        'TEACH': {
                            'count': 11,
                            'word-info': [[1, 'top']]
                        }
                    },
                    'words': {
                        0: ['MONK', 'MONK-N1', '$VAR0=0', 1],
                        1: ['TEACH', 'TEACH-V3', '$VAR0=1,$VAR1=0,$VAR2=2,$VAR3=4,$VAR4=3', 1],
                        2: ['YOU', 'YOU-N1', '$VAR0=2', 1],
                        4: ['BUDDHISM', 'BUDDHISM-N2', '$VAR0=4', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 4,
            'sentence': 'Monks teach you about Buddhism.',
            'timestamp': '2020-Mar-22 21:18:38'
        },


        {
            'OriginalSentence': 'I write poetry.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 2,
            'min-maxScores': [8.0, 14.5],
            'results': [
            {
                'TMR': {
                    'HUMAN-12': {
                        'AGENT-OF': 'WRITE-12',
                        'concept': 'HUMAN',
                        'from-sense': 'I-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [5, [0]],
                        'token': 'I'
                    },

                    'LITERARY-COMPOSITION-12': {
                        'HAS-STYLE': 'POEM',
                        'THEME-OF': 'WRITE-12',
                        'concept': 'LITERARY-COMPOSITION',
                        'from-sense': 'POETRY-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [5, [2]],
                        'token': 'poetry'
                    },

                    'WRITE-12': {
                        'AGENT': 'HUMAN-12',
                        'THEME': 'LITERARY-COMPOSITION-12',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'WRITE',
                        'from-sense': 'WRITE-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 5,
                        'sent-word-ind': [5, [1]],
                        'token': 'write'
                    },

                    'baseline-semantic-score': 2,
                    'combined-score': 14.5,
                    'semantic-score': 5,
                    'syntactic-score': 12.0
                },
                'concept_counts': {
                    'HUMAN': {
                        'count': 12,
                        'word-info': [[0, 'top']]
                    },
                    'LITERARY-COMPOSITION': {
                        'count':12,
                        'word-info': [[2, 'top']]
                    },
                    'WRITE': {
                        'count': 12,
                        'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['I', 'I-N1', '$VAR0=0', 1],
                    1: ['WRITE', 'WRITE-V1', '$VAR0=1,$VAR1=0,$VAR2=2,$VAR3=None', 1],
                    2: ['POETRY', 'POETRY-N1', '$VAR0=2', 1],
                    3: ['.', '.-PUNCT1', '$VAR0=3', 1]
                }
            }
        ],
        'sent-num': 5,
        'sentence': 'I write poetry.',
        'timestamp': '2020-Mar-22 21:18:38'
    },


    {
        'OriginalSentence': "You'd worsen the recession.",
        'ambiguous-words': {},
        'candidatesBeforePruning': 2,
        'min-maxScores': [8.0, 12.7],
        'results': [
            {
                'TMR': {
                    'CHANGE-EVENT-13': {
                        'CAUSED-BY': 'HUMAN-13',
                        'COMPARISON': '(<MODALITY-13.VALUE MODALITY-14.VALUE)',
                        'EFFECT': 'MODALITY-14',
                        'PRECONDITION':
                        'MODALITY-13',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'CHANGE-EVENT',
                        'from-sense': 'WORSEN-V2',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 2,
                        'sent-word-ind': [6, [2]],
                        'token': 'worsen'
                    },

                    'HUMAN-13': {
                        'EFFECT': 'CHANGE-EVENT-13',
                        'concept': 'HUMAN',
                        'from-sense': 'YOU-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [6, [0]],
                        'token': 'You'
                    },

                    'MODALITY-13': {
                        'PRECONDITION-OF': 'CHANGE-EVENT-13',
                        'SCOPE': 'RECESSION-13',
                        'TYPE': 'EVALUATIVE',
                        'concept': 'MODALITY',
                        'from-refsem': 'REFSEM1',
                        'from-sense': 'WORSEN-V2',
                        'sem-preference': 0,
                        'sent-word-ind': [6, [2]],
                        'token': 'worsen'
                    },

                    'MODALITY-14': {
                        'CAUSED-BY': 'CHANGE-EVENT-13',
                        'SCOPE': 'RECESSION-13',
                        'TYPE': 'EVALUATIVE',
                        'concept': 'MODALITY',
                        'from-refsem': 'REFSEM2',
                        'from-sense': 'WORSEN-V2',
                        'sem-preference': 0,
                        'sent-word-ind': [6, [2]],
                        'token': 'worsen'
                    },

                    'RECESSION-13': {
                        'SCOPE-OF': 'MODALITY-13',
                        'SCOPE-OF-1': 'MODALITY-14',
                        'concept': 'RECESSION',
                        'from-sense': 'RECESSION-N1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [6, [4]],
                        'token': 'recession'
                    },

                    'baseline-semantic-score': 3,
                    'combined-score': 12.67,
                    'semantic-score': 2,
                    'syntactic-score': 12.0
                },
                'concept_counts': {
                    'CHANGE-EVENT': {
                        'count': 13, 'word-info': [[2, 'top']]
                    },
                    'HUMAN': {
                        'count': 13,
                        'word-info': [[0, 'top']]
                    },
                    'MODALITY': {
                        'count': 14, 'word-info': [[2, 'REFSEM1'], [2, 'REFSEM2']]
                    },
                    'RECESSION': {
                        'count': 13, 'word-info': [[4, 'top']]
                    }
                },
                'words': {
                    0: ['YOU', 'YOU-N1', '$VAR0=0', 1],
                    1: ['WOULD', 'WOULD-AUX1', '$VAR0=1,$VAR1=2', 1],
                    2: ['WORSEN', 'WORSEN-V2',
                    '$VAR0=2,$VAR1=0,$VAR2=4', 1],
                    4: ['RECESSION', 'RECESSION-N1', '$VAR0=4', 1],
                    5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                }
            }
        ],
        'sent-num': 6,
        'sentence': "You'd worsen the recession.",
        'timestamp': '2020-Mar-22 21:18:38'
    },

    {
        'OriginalSentence': 'I worried about him.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 2,
        'min-maxScores': [12.0, 18.0],
        'results': [
            {
                'TMR': {
                    'HUMAN-15': {
                        'EXPERIENCER-OF': 'WORRY-15',
                        'concept': 'HUMAN',
                        'from-sense': 'I-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [7, [0]],
                        'token': 'I'
                    },
                    'HUMAN-16': {
                        'GENDER': 'MALE',
                        'THEME-OF': 'WORRY-15',
                        'concept': 'HUMAN',
                        'from-sense': 'HE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [7, [3]],
                        'token': 'him'
                    },
                    'WORRY-15': {
                        'EXPERIENCER': 'HUMAN-15',
                        'THEME': 'HUMAN-16',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'WORRY',
                        'from-sense': 'WORRY-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 4,
                        'sent-word-ind': [7, [1]],
                        'token': 'worried'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 18.0,
                    'semantic-score': 4,
                    'syntactic-score': 16.0
                },
                'concept_counts': {
                    'HUMAN': {
                        'count': 16,
                        'word-info': [[0, 'top'], [3, 'top']]
                    },
                    'WORRY': {
                        'count': 15,
                        'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['I', 'I-N1', '$VAR0=0', 1],
                    1: ['WORRY', 'WORRY-V1', '$VAR0=1,$VAR1=0,$VAR2=3,$VAR3=2', 1],
                    3: ['HE', 'HE-N1', '$VAR0=3', 1],
                    4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                }
            }
        ],
        'sent-num': 7,
        'sentence': 'I worried about him.',
        'timestamp': '2020-Mar-22 21:18:38'
    },


    {
        'OriginalSentence': "He worried about Turin's future.",
        'ambiguous-words': {},
        'candidatesBeforePruning': 4,
        'min-maxScores': [6.0, 22.0],
        'results': [
            {
                'TMR': {
                    'CITY-17': {
                        'HAS-NAME': 'TURIN',
                        'RELATION': 'TIME-INTERVAL-UNIT-17',
                        'concept': 'CITY',
                        'from-sense': 'OTHER-NAME',
                        'is-in-subtree': 'OBJECT',
                        'lex-source': 'onomasticon',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [8, [3]],
                        'token': 'Turin'
                    },
                    'HUMAN-17': {
                        'EXPERIENCER-OF': 'WORRY-17',
                        'GENDER': 'MALE',
                        'concept': 'HUMAN',
                        'from-sense': 'HE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [8, [0]],
                        'token': 'He'
                    },
                    'TIME-INTERVAL-UNIT-17': {
                        'THEME-OF': 'WORRY-17',
                        'RELATION': 'CITY-17',
                        'TIME': ['>', ['FIND-ANCHOR-TIME']],
                        'concept': 'TIME-INTERVAL-UNIT',
                        'from-sense': 'FUTURE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [8, [5]],
                        'token': 'future'
                    },
                    'WORRY-17': {
                        'EXPERIENCER': 'HUMAN-17',
                        'THEME': 'TIME-INTERVAL-UNIT-17',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'WORRY',
                        'from-sense': 'WORRY-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 4,
                        'sent-word-ind': [8, [1]],
                        'token': 'worried'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 22.0,
                    'semantic-score': 4,
                    'syntactic-score': 20.0
                },
                'concept_counts': {
                    'CITY': {
                        'count': 17, 'word-info':[[3, 'top']]
                    },
                    'HUMAN': {
                        'count': 17, 'word-info':[[0, 'top']]
                    },
                    'TIME-INTERVAL-UNIT': {
                        'count': 17, 'word-info': [[5, 'top']]
                    },
                    'WORRY': {
                        'count': 17, 'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['HE', 'HE-N1', '$VAR0=0', 1],
                    1: ['WORRY', 'WORRY-V1', '$VAR0=1,$VAR1=0,$VAR2=5,$VAR3=2', 1],
                    3: ['TURIN', 'OTHER-NAME', '$VAR0=3', 1],
                    5: ['FUTURE', 'FUTURE-N1', '$VAR0=5', 1],
                    6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                }
            }
        ],
        'sent-num': 8,
        'sentence': "He worried about Turin's future.",
        'timestamp': '2020-Mar-22 21:18:38'
    },

    {
        'OriginalSentence': "I'll work on the equipment.",
        'ambiguous-words': {},
        'candidatesBeforePruning': 4,
        'min-maxScores': [2.0, 18.0],
        'results': [
            {
                'TMR': {
                    'DEVICE-18': {
                        'THEME-OF': 'WORK-ACTIVITY-18',
                        'concept': 'DEVICE',
                        'from-sense': 'EQUIPMENT-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [9, [5]],
                        'token': 'equipment'
                    },
                    'HUMAN-18': {
                        'AGENT-OF': 'WORK-ACTIVITY-18',
                        'concept': 'HUMAN',
                        'from-sense': 'I-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [9, [0]],
                        'token': 'I'
                    },
                    'WORK-ACTIVITY-18': {
                        'AGENT': 'HUMAN-18',
                        'THEME': 'DEVICE-18',
                        'TIME': ['>', 'FIND-ANCHOR-TIME'],
                        'concept': 'WORK-ACTIVITY',
                        'from-sense': 'WORK-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 4,
                        'sent-word-ind': [9, [2]],
                        'token': 'work'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 18.0,
                    'semantic-score': 4,
                    'syntactic-score': 16.0
                },
                'concept_counts': {
                    'DEVICE': {
                        'count': 18, 'word-info': [[5, 'top']]
                    },
                    'HUMAN': {
                        'count': 18, 'word-info': [[0, 'top']]
                    },
                    'WORK-ACTIVITY': {
                        'count': 18,
                        'word-info': [[2, 'top']]
                    }
                },
                'words': {
                    0: ['I', 'I-N1', '$VAR0=0', 1],
                    1: ['WILL', 'WILL-AUX1', '$VAR0=1,$VAR1=2', 1],
                    2: ['WORK', 'WORK-V1', '$VAR0=2,$VAR1=0,$VAR2=5,$VAR3=3,$VAR4=None,$VAR5=None', 1],
                    5: ['EQUIPMENT', 'EQUIPMENT-N1', '$VAR0=5', 1],
                    6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                }
            }
        ],
        'sent-num': 9,
        'sentence': "I'll work on the equipment.",
        'timestamp': '2020-Mar-22 21:18:38'
    },

    {
        'OriginalSentence': 'We work and we eat.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 108,
        'min-maxScores': [3.0, 26.0],
        'results': [
            {
                'TMR': {
                    'DISCOURSE-RELATION-19': {
                        'DOMAIN': 'WORK-ACTIVITY-19',
                        'RANGE': 'INGEST-19',
                        'concept': 'DISCOURSE-RELATION',
                        'from-sense': 'AND-CONJ1',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 9.0,
                        'sem-preference': 0,
                        'sent-word-ind': [10, [2]],
                        'token': 'and'
                    },
                    'INGEST-19': {
                        'AGENT': 'SET-20',
                        'RANGE-OF': 'DISCOURSE-RELATION-19',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'INGEST',
                        'from-sense': 'EAT-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 2,
                        'sent-word-ind': [10, [4]],
                        'token': 'eat'
                    },
                    'SET-19': {
                        'AGENT-OF': 'WORK-ACTIVITY-19',
                        'CARDINALITY': ['>', 1],
                        'MEMBER-TYPE': 'HUMAN',
                        'concept': 'SET',
                        'from-sense': 'WE-N1',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [10, [0]],
                        'sponsor-of': 'SET-20',
                        'token': 'We'
                    },
                    'SET-20': {
                        'AGENT-OF': 'INGEST-19',
                        'CARDINALITY': ['>', 1],
                        'MEMBER-TYPE': 'HUMAN',
                        'concept': 'SET',
                        'coref': [],
                        'from-sense': 'WE-N1',
                        'has-sponsor': 'SET-19',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [10, [3]],
                        'token': 'we'
                    },
                    'TotalSynRefScore': 0.95,
                    'WORK-ACTIVITY-19': {
                        'AGENT': 'SET-19',
                        'DOMAIN-OF': 'DISCOURSE-RELATION-19',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'WORK-ACTIVITY',
                        'from-sense': 'WORK-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 2,
                        'sent-word-ind': [10,[1]],
                        'token': 'work'
                    },
                    'baseline-semantic-score': 4,
                    'combined-score': 26.0,
                    'semantic-score': 4,
                    'syntactic-score': 25.0
                },
                'concept_counts': {
                    'DISCOURSE-RELATION': {
                        'count': 19,
                        'word-info': [[2, 'top']]
                    },
                    'INGEST': {
                        'count': 19, 'word-info': [[4, 'top']]
                    },
                    'SET': {
                        'count': 21, 'word-info': [[0, 'top'], [3, 'top'], [2, 'top']]
                    },
                    'WORK-ACTIVITY': {
                        'count': 19, 'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['WE', 'WE-N1', '$VAR0=0', 1],
                    1: ['WORK', 'WORK-V1', '$VAR0=1,$VAR1=0,$VAR2=None,$VAR3=None,$VAR4=None,$VAR5=None', 1],
                    2: ['AND', 'AND-CONJ1', '$VAR0=2,$VAR1=1,$VAR2=4,$VAR3=None', 1],
                    3: ['WE', 'WE-N1', '$VAR0=3', 1],
                    4: ['EAT', 'EAT-V1', '$VAR0=4,$VAR2=3,$VAR3=None', 1],
                    5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                }
            }
        ],
        'sent-num': 10,
        'sentence': 'We work and we eat.',
        'timestamp': '2020-Mar-22 21:18:38'
    },

    {
        'OriginalSentence': 'I work fast.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 6,
        'min-maxScores': [7.0, 13.7],
        'results': [
            {
                'TMR': {
                    'HUMAN-22': {
                        'AGENT-OF': 'WORK-ACTIVITY-22',
                        'concept': 'HUMAN',
                        'from-sense': 'I-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [11, [0]],
                        'token': 'I'
                    },
                    'WORK-ACTIVITY-22': {
                        'AGENT': 'HUMAN-22',
                        'RAPIDITY': 0.8,
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'WORK-ACTIVITY',
                        'from-sense': 'WORK-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 5,
                        'sent-word-ind': [11, [1,2]],
                        'token': 'work'
                    },
                    'baseline-semantic-score': 3,
                    'combined-score': 13.67,
                    'semantic-score': 5,
                    'syntactic-score': 12.0},
                    'concept_counts': {
                        'HUMAN': {
                            'count': 22,
                            'word-info': [[0, 'top']]
                        },
                        'WORK-ACTIVITY': {
                            'count': 22,
                            'word-info': [[1,'top']]
                        }
                    },
                    'words': {
                        0: ['I', 'I-N1', '$VAR0=0', 1],
                        1: ['WORK', 'WORK-V1', '$VAR0=1,$VAR1=0,$VAR2=None,$VAR3=None,$VAR4=None,$VAR5=None', 1],
                        2: ['FAST', 'FAST-ADV1', '$VAR0=2,$VAR1=1', 1],
                        3: ['.', '.-PUNCT1', '$VAR0=3', 1]
                    }
                }
            ],
            'sent-num': 11,
            'sentence': 'I work fast.',
            'timestamp': '2020-Mar-22 21:18:38'
        },

        {
            'OriginalSentence': 'The team won the championship.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 10,
            'min-maxScores': [5.0, 12.0],
            'results': [
            {
                'TMR': {
                    'EVENT-23': {
                        'THEME-OF': 'WIN-23',
                        'concept': 'EVENT',
                        'from-sense': 'DEFAULT_NOUN-N2',
                        'is-in-subtree': 'EVENT',
                        'preference': 2.0,
                        'sem-preference': 0,
                        'sent-word-ind': [12, [4]],
                        'token': 'championship'
                    },
                    'SPORTS-TEAM-23': {
                        'AGENT-OF': 'WIN-23',
                        'concept': 'SPORTS-TEAM',
                        'from-sense': 'TEAM-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [12, [1]],
                        'token': 'team'
                    },
                    'WIN-23': {
                        'AGENT': 'SPORTS-TEAM-23',
                        'THEME': 'EVENT-23',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'WIN',
                        'from-sense': 'WIN-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [12, [2]],
                        'token': 'won'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 12.0,
                    'semantic-score': 4,
                    'syntactic-score': 10.0},
                    'concept_counts': {
                        'EVENT': {
                            'count': 23,
                            'word-info': [[4, 'top']]
                        },
                        'SPORTS-TEAM': {
                            'count': 23,
                            'word-info': [[1, 'top']]
                        },
                        'WIN': {
                            'count': 23,
                            'word-info': [[2, 'top']]
                        }
                    },
                    'words': {
                        1: ['TEAM', 'TEAM-N1', '$VAR0=1', 1],
                        2: ['WIN', 'WIN-V1', '$VAR0=2,$VAR1=1,$VAR2=4', 1],
                        4: ['CHAMPIONSHIP', 'DEFAULT_NOUN-N2', '$VAR0=4', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 12,
            'sentence': 'The team won the championship.',
            'timestamp': '2020-Mar-22 21:18:38'
        },


        {
            'OriginalSentence': 'Everybody should watch out.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 2,
            'min-maxScores': [12.0, 18.0],
            'results': [
                {
                    'TMR': {
                        'BEWARE-24': {
                            'AGENT': 'SET-24',
                            'SCOPE-OF': 'MODALITY-24',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'BEWARE',
                            'from-sense': 'WATCH-V3',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 2,
                            'sent-word-ind': [13, [2]],
                            'token': 'watch'
                        },
                        'MODALITY-24': {
                            'ATTRIBUTED-TO': '*SPEAKER*',
                            'SCOPE': 'BEWARE-24',
                            'TYPE': 'OBLIGATIVE',
                            'VALUE': 0.7,
                            'concept': 'MODALITY',
                            'from-sense': 'SHOULD-AUX1',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [13, [1]],
                            'token': 'should'
                        },
                        'SET-24': {
                            'AGENT-OF': 'BEWARE-24',
                            'CARDINALITY': 1,
                            'COMPLETE': 'YES',
                            'MEMBER-TYPE': 'HUMAN',
                            'concept': 'SET',
                            'from-sense': 'EVERYBODY-N2',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [13, [0]],
                            'token': 'Everybody'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 18.0,
                        'semantic-score': 4,
                        'syntactic-score': 16.0
                    },
                    'concept_counts': {
                        'BEWARE': {
                            'count': 24,
                            'word-info': [[2, 'top']]
                        },
                        'MODALITY': {
                            'count': 24,
                            'word-info': [[1, 'top']]
                        },
                        'SET': {
                            'count': 24,
                            'word-info': [[0, 'top']]
                        }
                    },
                    'words': {
                        0: ['EVERYBODY', 'EVERYBODY-N2', '$VAR0=0', 1],
                        1: ['SHOULD', 'SHOULD-AUX1', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                        2: ['WATCH', 'WATCH-V3', '$VAR0=2,$VAR1=0,$VAR2=3,$VAR3=None,$VAR4=None', 1],
                        4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                    }
                }
            ],
            'sent-num': 13,
            'sentence': 'Everybody should watch out.',
            'timestamp': '2020-Mar-22 21:18:38'
        },


        {
            'OriginalSentence': 'They should wake you up.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 12,
            'min-maxScores': [11.0, 22.0],
            'results': [
                {
                    'TMR': {
                        'CHANGE-EVENT-25': {
                            'CAUSED-BY': 'SET-25',
                            'EFFECT': 'SLEEP-26',
                            'PRECONDITION': 'SLEEP-25',
                            'SCOPE-OF': 'MODALITY-25',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'CHANGE-EVENT',
                            'from-sense': 'WAKE-V3',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 2,
                            'sent-word-ind': [14, [2]],
                            'token': 'wake'
                        },
                        'HUMAN-25': {
                            'EXPERIENCER-OF': 'SLEEP-26',
                            'EXPERIENCER-OF-1': 'SLEEP-25',
                            'concept': 'HUMAN',
                            'from-sense': 'YOU-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [14, [3]],
                            'token': 'you'
                        },
                        'MODALITY-25': {
                            'ATTRIBUTED-TO': '*SPEAKER*',
                            'SCOPE': 'CHANGE-EVENT-25',
                            'TYPE': 'OBLIGATIVE',
                            'VALUE': 0.7,
                            'concept': 'MODALITY',
                            'from-sense': 'SHOULD-AUX1',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [14, [1]],
                            'token': 'should'
                        },
                        'MODALITY-26': {
                            'SCOPE': 'SLEEP-26',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'TYPE': 'EPISTEMIC',
                            'VALUE': 0,
                            'concept': 'MODALITY',
                            'from-sense': 'WAKE-V3',
                            'sem-preference': 0,
                            'sent-word-ind': [14, [2]],
                            'token': 'wake'
                        },
                        'SET-25': {
                            'CARDINALITY': ['>', 1],
                            'EFFECT': 'CHANGE-EVENT-25',
                            'MEMBER-TYPE': 'ALL',
                            'concept': 'SET',
                            'from-sense': 'THEY-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [14, [0]],
                            'token': 'They'
                        },
                        'SLEEP-25': {
                            'EXPERIENCER': 'HUMAN-25',
                            'PRECONDITION-OF': 'CHANGE-EVENT-25',
                            'concept': 'SLEEP',
                            'from-refsem': 'REFSEM1',
                            'from-sense': 'WAKE-V3',
                            'sem-preference': 2,
                            'sent-word-ind': [14, [2]],
                            'token': 'wake'
                        },
                        'SLEEP-26': {
                            'CAUSED-BY': 'CHANGE-EVENT-25',
                            'EXPERIENCER': 'HUMAN-25',
                            'concept': 'SLEEP',
                            'from-refsem': 'REFSEM2',
                            'from-sense': 'WAKE-V3',
                            'sem-preference': 2,
                            'sent-word-ind': [14, [2]],
                            'token': 'wake'
                        },
                        'baseline-semantic-score': 4,
                        'combined-score': 22.0,
                        'semantic-score': 8,
                        'syntactic-score': 20.0
                    },
                    'concept_counts': {
                        'CHANGE-EVENT': {
                            'count': 25,
                            'word-info': [[2, 'top']]
                        },
                        'HUMAN': {
                            'count': 25,
                            'word-info': [[3, 'top']]
                        },
                        'MODALITY': {
                            'count': 26,
                            'word-info': [[1, 'top'], [2, 'top']]
                        },
                        'SET': {
                            'count': 25,
                            'word-info': [[0, 'top']]
                        },
                        'SLEEP': {
                            'count': 26,
                            'word-info': [[1001, 'top'], [1002, 'top']]
                        }
                    },
                    'words': {
                        0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                        1: ['SHOULD', 'SHOULD-AUX1', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                        2: ['WAKE', 'WAKE-V3', '$VAR0=2,$VAR1=0,$VAR2=4,$VAR3=3', 1],
                        3: ['YOU', 'YOU-N1', '$VAR0=3', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 14,
            'sentence': 'They should wake you up.',
            'timestamp': '2020-Mar-22 21:18:38'
        },


        {
            'OriginalSentence': 'I slept till I woke up.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 1,
            'min-maxScores': [26.0, 26.0],
            'results': [
                {
                    'TMR': {
                        'ASPECT-27': {
                            'PHASE': 'END',
                            'SCOPE': 'SLEEP-28',
                            'concept': 'ASPECT',
                            'from-sense': 'WAKE-V2',
                            'sem-preference': 0,
                            'sent-word-ind': [15, [4]],
                            'token': 'woke'
                        },
                        'HUMAN-27': {
                            'EXPERIENCER-OF': 'SLEEP-27',
                            'concept': 'HUMAN',
                            'from-sense': 'I-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [15, [0]],
                            'token': 'I'
                        },
                        'HUMAN-28': {
                            'EXPERIENCER-OF': 'SLEEP-28',
                            'concept': 'HUMAN',
                            'coref': [],
                            'from-sense': 'I-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [15, [3]],
                            'token': 'I'
                        },
                        'SLEEP-27': {
                            'EXPERIENCER': 'HUMAN-27',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'TIME-1': ['<', 'SLEEP-28.TIME'],
                            'concept': 'SLEEP',
                            'from-sense': 'SLEEP-V1',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 4,
                            'sent-word-ind': [15, [1, 2]],
                            'token': 'slept'
                        },
                        'SLEEP-28': {
                            'EXPERIENCER': 'HUMAN-28',
                            'SCOPE-OF': 'ASPECT-27',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'SLEEP',
                            'from-sense': 'WAKE-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 4,
                            'sent-word-ind': [15, [4]],
                            'token': 'woke'
                        },
                        'baseline-semantic-score': 4,
                        'combined-score': 26.0,
                        'semantic-score': 8,
                        'syntactic-score': 24.0
                    },
                    'concept_counts': {
                        'ASPECT': {
                            'count': 27,
                            'word-info': [[4, 'top']]
                        },
                        'HUMAN': {
                            'count': 28,
                            'word-info': [[0, 'top'], [3, 'top']]
                        },
                        'SLEEP': {
                            'count': 28,
                            'word-info': [[1, 'top'], [4, 'top']]
                        }
                    },
                    'words': {
                        0: ['I', 'I-N1', '$VAR0=0', 1],
                        1: ['SLEEP', 'SLEEP-V1', '$VAR0=1,$VAR1=0', 1],
                        2: ['TILL', 'UNTIL-CONJ1', '$VAR0=2,$VAR1=1,$VAR2=4', 1],
                        3: ['I', 'I-N1', '$VAR0=3', 1],
                        4: ['WAKE', 'WAKE-V2', '$VAR0=4,$VAR1=3,$VAR2=5', 1],
                        6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                    }
                }
            ],
            'sent-num': 15,
            'sentence': 'I slept till I woke up.',
            'timestamp': '2020-Mar-22 21:18:38'
        },


        {
            'OriginalSentence': 'Jack wakes up with Jennifer.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 12,
            'min-maxScores': [17.3, 22.0],
            'results': [
                {
                    'TMR': {
                        'ASPECT-29': {
                            'PHASE': 'END',
                            'SCOPE': 'SLEEP-29',
                            'concept': 'ASPECT',
                            'from-sense': 'WAKE-V2',
                            'sem-preference': 0,
                            'sent-word-ind': [16, [1]],
                            'token': 'wakes'
                        },
                        'HUMAN-29': {
                            'EXPERIENCER-OF': 'SLEEP-29',
                            'GENDER': 'MALE',
                            'HAS-PERSONAL-NAME': 'JACK',
                            'concept': 'HUMAN',
                            'from-sense': 'PERSON-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'NER',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [16, [0]],
                            'token': 'Jack'
                        },
                        'HUMAN-30': {
                            'BESIDE-INVERSE': 'SLEEP-29',
                            'GENDER': 'FEMALE',
                            'HAS-PERSONAL-NAME': 'JENNIFER',
                            'concept': 'HUMAN',
                            'from-sense': 'PERSON-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'NER',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [16, [4]],
                            'token': 'Jennifer'
                        },
                        'SLEEP-29': {
                            'BESIDE': 'HUMAN-30',
                            'EXPERIENCER': 'HUMAN-29',
                            'SCOPE-OF': 'ASPECT-29',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'SLEEP',
                            'from-sense': 'WAKE-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 12.0,
                            'sem-preference': 6,
                            'sent-word-ind': [16, [1, 3]],
                            'token': 'wakes'
                        },
                        'baseline-semantic-score': 3,
                        'combined-score': 22.0,
                        'semantic-score': 6,
                        'syntactic-score': 20.0
                    },
                    'concept_counts': {
                        'ASPECT': {
                            'count': 29,
                            'word-info': [[1, 'top']]
                        },
                        'HUMAN': {
                            'count': 30,
                            'word-info': [[0, 'top'], [4, 'top']]
                        },
                        'SLEEP': {
                            'count': 29,
                            'word-info': [[1, 'top']]
                        }
                    },
                    'words': {
                        0: ['JACK', 'PERSON-NAME', '$VAR0=0', 1],
                        1: ['WAKE', 'WAKE-V2', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                        3: ['WITH', 'WITH-PREP2', '$VAR0=3,$VAR1=1,$VAR2=4', 1],
                        4: ['JENNIFER', 'PERSON-NAME', '$VAR0=4', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 16,
            'sentence': 'Jack wakes up with Jennifer.',
            'timestamp': '2020-Mar-22 21:18:39'
        },


        {
            'OriginalSentence': 'He has visited Cincinnati, Tennessee and Miami.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 3,
            'min-maxScores': [28.0, 34.5],
            'results': [
                {
                    'TMR': {
                        'ASPECT-31': {
                            'PHASE': 'BEGIN-CONTINUE-END',
                            'SCOPE': 'COME-31',
                            'concept': 'ASPECT',
                            'from-sense': 'HAVE-AUX2',
                            'sem-preference': 0,
                            'sent-word-ind': [17, [1]],
                            'token': 'has'
                        },
                        'CITY-31': {
                            'ELEMENTS-OF': 'SET-31',
                            'HAS-NAME': 'CINCINNATI',
                            'concept': 'CITY',
                            'from-sense': 'OTHER-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'onomasticon',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [17, [3]],
                            'token': 'Cincinnati'
                        },
                        'CITY-32': {
                            'ELEMENTS-OF': 'SET-31',
                            'HAS-NAME': 'MIAMI',
                            'concept': 'CITY',
                            'from-sense': 'OTHER-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'onomasticon',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [17, [7]],
                            'token': 'Miami'
                        },
                        'COME-31': {
                            'AGENT': 'HUMAN-31',
                            'DESTINATION': 'SET-31',
                            'SCOPE-OF': 'ASPECT-31',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'COME',
                            'from-sense': 'VISIT-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 5,
                            'sent-word-ind': [17, [2, 1]],
                            'token': 'visited'
                        },
                        'HUMAN-31': {
                            'AGENT-OF': 'COME-31',
                            'GENDER': 'MALE',
                            'concept': 'HUMAN',
                            'from-sense': 'HE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [17, [0]],
                            'token': 'He'
                        },
                        'SET-31': {
                            'DESTINATION-OF': 'COME-31',
                            'ELEMENTS': ['CITY-31', 'STATE-31', 'CITY-32'],
                            'concept': 'SET',
                            'from-sense': 'AND-CONJ8',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 8.0,
                            'sem-preference': 0,
                            'sent-word-ind': [17, [6]],
                            'token': 'and'
                        },
                        'STATE-31': {
                            'ELEMENTS-OF': 'SET-31',
                            'HAS-NAME': 'TENNESSEE',
                            'concept': 'STATE',
                            'from-sense': 'TENNESSEE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [17, [5]],
                            'token': 'Tennessee'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 34.5,
                        'semantic-score': 5,
                        'syntactic-score': 32.0
                    },
                    'concept_counts': {
                        'ASPECT': {
                            'count': 31, 'word-info': [[1, 'top']]
                        },
                        'CITY': {
                            'count': 32, 'word-info': [[3, 'top'], [7, 'top']]
                        },
                        'COME': {
                            'count': 31, 'word-info': [[2, 'top']]
                        },
                        'HUMAN': {
                            'count': 31, 'word-info': [[0, 'top']]
                        },
                        'SET': {
                            'count': 31, 'word-info': [[6, 'top']]
                        },
                        'STATE': {
                            'count': 31, 'word-info': [[5, 'top']]
                        }
                    },
                    'words': {
                        0: ['HE', 'HE-N1', '$VAR0=0', 1],
                        1: ['HAVE', 'HAVE-AUX2', '$VAR0=1,$VAR1=2', 1],
                        2: ['VISIT', 'VISIT-V2', '$VAR0=2,$VAR1=0,$VAR2=3', 1],
                        3: ['CINCINNATI', 'OTHER-NAME', '$VAR0=3', 1],
                        4: [',', ',-PUNCT1', '$VAR0=4', 1],
                        5: ['TENNESSEE', 'TENNESSEE-N1', '$VAR0=5', 1],
                        6: ['AND', 'AND-CONJ8', '$VAR0=6,$VAR1=3,$VAR2=4,$VAR3=5,$VAR4=None,$VAR5=7', 1],
                        7: ['MIAMI', 'OTHER-NAME', '$VAR0=7', 1],
                        8: ['.', '.-PUNCT1', '$VAR0=8', 1]
                    }
                }
            ],
            'sent-num': 17,
            'sentence': 'He has visited Cincinnati, Tennessee and Miami.',
            'timestamp': '2020-Mar-22 21:18:39'
        },


        {
            'OriginalSentence': 'They visited the crime scenes.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 9,
            'min-maxScores': [10.0, 18.3],
            'results': [
                {
                    'TMR': {
                        'COME-33': {
                            'AGENT': 'SET-33',
                            'DESTINATION': 'PLACE-33',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'COME',
                            'from-sense': 'VISIT-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 5,
                            'sent-word-ind': [18, [1]],
                            'token': 'visited'
                        },
                        'CRIMINAL-ACTIVITY-33': {
                            'LOCATION': 'PLACE-33',
                            'concept': 'CRIMINAL-ACTIVITY',
                            'from-sense': 'CRIME-N1',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [18, [3]],
                            'token': 'crime'
                        },
                        'PLACE-33': {
                            'CARDINALITY': ['>', 1],
                            'DESTINATION-OF': 'COME-33',
                            'LOCATION-OF': 'CRIMINAL-ACTIVITY-33',
                            'concept': 'PLACE',
                            'from-sense': 'SCENE-N2',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [18, [4]],
                            'token': 'scenes'
                        },
                        'SET-33': {
                            'AGENT-OF': 'COME-33',
                            'CARDINALITY': ['>', 1],
                            'MEMBER-TYPE': 'ALL',
                            'concept': 'SET',
                            'from-sense': 'THEY-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [18, [0]],
                            'token': 'They'
                        },
                        'baseline-semantic-score': 3,
                        'combined-score': 18.33,
                        'semantic-score': 7,
                        'syntactic-score': 16.0
                    },
                    'concept_counts': {
                        'COME': {
                            'count': 33,
                            'word-info': [[1, 'top']]
                        },
                        'CRIMINAL-ACTIVITY': {
                            'count': 33,
                            'word-info': [[3, 'top']]
                        },
                        'PLACE': {
                            'count': 33,
                            'word-info': [[4, 'top']]
                        },
                        'SET': {
                            'count': 33,
                            'word-info': [[0, 'top']]
                        }
                    },
                    'words': {
                        0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                        1: ['VISIT', 'VISIT-V2', '$VAR0=1,$VAR1=0,$VAR2=4', 1],
                        3: ['CRIME', 'CRIME-N1', '$VAR0=3', 1],
                        4: ['SCENE', 'SCENE-N2', '$VAR0=4,$VAR1=3', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 18,
            'sentence': 'They visited the crime scenes.',
            'timestamp': '2020-Mar-22 21:18:39'
        },


        {
            'OriginalSentence': 'Ghosts visit a grumpy TV executive.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 3,
            'min-maxScores': [13.7, 21.7],
            'results': [
                {
                    'TMR': {
                        'COME-34': {
                            'AGENT': 'GHOST-34',
                            'DESTINATION': 'EXECUTIVE-34',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'COME',
                            'from-sense': 'VISIT-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 4,
                            'sent-word-ind': [19, [1]],
                            'token': 'visit'
                        },
                        'EXECUTIVE-34': {
                            'DESTINATION-OF': 'COME-34',
                            'EMOTIONAL-STATE': 0.3,
                            'RANGE-OF': 'RELATION-34',
                            'concept': 'EXECUTIVE',
                            'from-sense': 'EXECUTIVE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 8.0,
                            'sem-preference': 1,
                            'sent-word-ind': [19, [5, 3]],
                            'token': 'executive'
                        },
                        'GHOST-34': {
                            'AGENT-OF': 'COME-34',
                            'CARDINALITY': ['>', 1],
                            'concept': 'GHOST',
                            'from-sense': 'GHOST-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [19, [0]],
                            'token': 'Ghosts'
                        },
                        'RELATION-34': {
                            'DOMAIN': 'TELEVISION-34',
                            'RANGE': 'EXECUTIVE-34',
                            'concept': 'RELATION',
                            'is-in-subtree': 'PROPERTY',
                            'sem-preference': 0
                        },
                        'TELEVISION-34': {
                            'DOMAIN-OF': 'RELATION-34',
                            'concept': 'TELEVISION',
                            'from-sense':
                            'TELEVISION_SET-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [19, [4]],
                            'token': 'TV'
                        },
                        'baseline-semantic-score': 3,
                        'combined-score': 21.67,
                        'semantic-score': 5,
                        'syntactic-score': 20.0},
                        'concept_counts': {
                            'COME': {
                                'count': 34,
                                'word-info': [[1, 'top']]
                            },
                            'EXECUTIVE': {
                                'count': 34,
                                'word-info': [[5, 'top']]
                            },
                            'GHOST': {
                                'count': 34,
                                'word-info': [[0, 'top']]
                            },
                            'TELEVISION': {
                                'count': 34,
                                'word-info': [[4, 'top']]
                            }
                        },
                        'words': {
                            0: ['GHOST', 'GHOST-N1', '$VAR0=0', 1],
                            1: ['VISIT', 'VISIT-V2', '$VAR0=1,$VAR1=0,$VAR2=5', 1],
                            3: ['GRUMPY', 'DISCONTENT-ADJ1', '$VAR0=3,$VAR1=5', 1],
                            4: ['TV', 'TELEVISION_SET-N1', '$VAR0=4', 1],
                            5: ['EXECUTIVE', 'EXECUTIVE-N1', '$VAR0=5', 1],
                            6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                        }
                    }
                ],
                'sent-num': 19,
                'sentence': 'Ghosts visit a grumpy TV executive.',
                'timestamp': '2020-Mar-22 21:18:39'
            },


            {
                'OriginalSentence': 'Thoreen turned down the offer.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 7,
                'min-maxScores': [-8.0, 18.0],
                'results': [
                    {
                        'TMR': {
                            'ACCEPT-35': {
                                'AGENT': 'HUMAN-35',
                                'SCOPE-OF': 'MODALITY-35',
                                'THEME': 'PROPOSE-35',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'ACCEPT',
                                'from-sense': 'TURN-V11',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 4,
                                'sent-word-ind': [20, [1]],
                                'token': 'turned'
                            },
                            'HUMAN-35': {
                                'AGENT-OF': 'ACCEPT-35',
                                'HAS-PERSONAL-NAME': 'THOREEN',
                                'concept': 'HUMAN',
                                'from-sense': 'PERSON-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'NER',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [20, [0]],
                                'token': 'Thoreen'
                            },
                            'MODALITY-35': {
                                'SCOPE': 'ACCEPT-35',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'TYPE': 'EPISTEMIC',
                                'VALUE': 0,
                                'concept': 'MODALITY',
                                'from-sense': 'TURN-V11',
                                'sem-preference': 0,
                                'sent-word-ind': [20, [1]],
                                'token': 'turned'
                            },
                            'PROPOSE-35': {
                                'THEME-OF': 'ACCEPT-35',
                                'concept': 'PROPOSE',
                                'from-sense': 'OFFER-N1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [20, [4]],
                                'token': 'offer'
                            },
                    'baseline-semantic-score': 2,
                    'combined-score': 18.0,
                    'semantic-score': 4,
                    'syntactic-score': 16.0
                },
                'concept_counts': {
                    'ACCEPT': {
                        'count': 35,
                        'word-info': [[1, 'top']]
                    },
                    'HUMAN': {
                        'count': 35,
                        'word-info': [[0, 'top']]
                    },
                    'MODALITY': {
                        'count': 35,
                        'word-info': [[1, 'top']]
                    },
                    'PROPOSE': {
                        'count': 35,
                        'word-info': [[4, 'top']]
                    }
                },
                'words': {
                    0: ['THOREEN', 'PERSON-NAME', '$VAR0=0', 1],
                    1: ['TURN', 'TURN-V11', '$VAR0=1,$VAR1=0,$VAR2=4,$VAR3=2', 1],
                    4: ['OFFER', 'OFFER-N1', '$VAR0=4,$VAR1=None,$VAR2=None,$VAR3=None', 1],
                    5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                }
            }
        ],
        'sent-num': 20,
        'sentence': 'Thoreen turned down the offer.',
        'timestamp': '2020-Mar-22 21:18:39'
    },


    {
        'OriginalSentence': 'You use onion, garlic and cumin.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 4,
        'min-maxScores': [24.0, 30.0],
        'results': [
            {
                'TMR': {
                    'CUMIN-36': {
                        'ELEMENTS-OF': 'SET-36',
                        'concept': 'CUMIN',
                        'from-sense': 'CUMIN-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [21, [6]],
                        'token': 'cumin'
                    },
                    'EVENT-36': {
                        'AGENT': 'HUMAN-36',
                        'INSTRUMENT': 'SET-36',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'EVENT',
                        'from-sense': 'USE-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [21, [1]],
                        'token': 'use'
                    },
                    'GARLIC-36': {
                        'ELEMENTS-OF': 'SET-36',
                        'concept': 'GARLIC',
                        'from-sense': 'GARLIC-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [21, [4]],
                        'token': 'garlic'
                    },
                    'HUMAN-36': {
                        'AGENT-OF': 'EVENT-36',
                        'concept': 'HUMAN',
                        'from-sense': 'YOU-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [21, [0]],
                        'token': 'You'
                    },
                    'ONION-36': {
                        'ELEMENTS-OF': 'SET-36',
                        'concept': 'ONION',
                        'from-sense': 'ONION-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [21, [2]],
                        'token': 'onion'
                    },
                    'SET-36': {
                        'ELEMENTS': ['ONION-36',
                        'GARLIC-36', 'CUMIN-36'],
                        'INSTRUMENT-OF': 'EVENT-36',
                        'concept': 'SET',
                        'from-sense': 'AND-CONJ8',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 8.0,
                        'sem-preference': 0,
                        'sent-word-ind': [21, [5]],
                        'token': 'and'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 30.0,
                    'semantic-score': 4,
                    'syntactic-score': 28.0
                },
                'concept_counts': {
                    'CUMIN': {
                        'count': 36,
                        'word-info': [[6, 'top']]
                    },
                    'EVENT': {
                        'count': 36,
                        'word-info': [[1, 'top']]
                    },
                    'GARLIC': {
                        'count': 36,
                        'word-info': [[4, 'top']]
                    },
                    'HUMAN': {
                        'count': 36,
                        'word-info': [[0, 'top']]
                    },
                    'ONION': {
                        'count': 36,
                        'word-info': [[2, 'top']]
                    },
                    'SET': {
                        'count': 36,
                        'word-info': [[5, 'top']]
                    }
                },
                'words': {
                    0: ['YOU', 'YOU-N1', '$VAR0=0', 1],
                    1: ['USE', 'USE-V1', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                    2: ['ONION', 'ONION-N1', '$VAR0=2', 1],
                    3: [',', ',-PUNCT1', '$VAR0=3', 1],
                    4: ['GARLIC', 'GARLIC-N1', '$VAR0=4', 1],
                    5: ['AND', 'AND-CONJ8', '$VAR0=5,$VAR1=2,$VAR2=3,$VAR3=4,$VAR4=None,$VAR5=6', 1],
                    6: ['CUMIN', 'CUMIN-N1', '$VAR0=6', 1],
                    7: ['.', '.-PUNCT1', '$VAR0=7', 1]
                }
            }
        ],
        'sent-num': 21,
        'sentence': 'You use onion, garlic and cumin.',
        'timestamp': '2020-Mar-22 21:18:39'
    },


    {
        'OriginalSentence': 'He turns off the engine.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 11,
        'min-maxScores': [-7.0, 18.0],
        'results': [
            {
                'TMR': {
                    'ENGINE-37': {
                        'THEME-OF': 'TURN-SWITCH-OFF-37',
                        'concept': 'ENGINE',
                        'from-sense': 'ENGINE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [22, [4]],
                        'token': 'engine'
                    },
                    'HUMAN-37': {
                        'AGENT-OF': 'TURN-SWITCH-OFF-37',
                        'GENDER': 'MALE',
                        'concept': 'HUMAN',
                        'from-sense': 'HE-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [22, [0]],
                        'token': 'He'
                    },
                    'TURN-SWITCH-OFF-37': {
                        'AGENT': 'HUMAN-37',
                        'THEME': 'ENGINE-37',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'TURN-SWITCH-OFF',
                        'from-sense': 'TURN-V6',
                        'is-in-subtree': 'EVENT',
                        'preference': 8.0,
                        'sem-preference': 4,
                        'sent-word-ind': [22, [1]],
                        'token': 'turns'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 18.0,
                    'semantic-score': 4,
                    'syntactic-score': 16.0
                },
                'concept_counts': {
                    'ENGINE': {
                        'count': 37,
                        'word-info': [[4, 'top']]
                    },
                    'HUMAN': {
                        'count': 37,
                        'word-info': [[0, 'top']]
                    },
                    'TURN-SWITCH-OFF': {
                        'count': 37,
                        'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['HE', 'HE-N1', '$VAR0=0', 1],
                    1: ['TURN', 'TURN-V6', '$VAR0=1,$VAR1=0,$VAR2=4,$VAR3=2', 1],
                    4: ['ENGINE', 'ENGINE-N1', '$VAR0=4', 1],
                    5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                }
            }
        ],
        'sent-num': 22,
        'sentence': 'He turns off the engine.',
        'timestamp': '2020-Mar-22 21:18:39'
    },


    {
        'OriginalSentence': 'Somebody turned on a television.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 14,
        'min-maxScores': [-5.0, 17.4],
        'results': [
            {
                'TMR': {
                    'HUMAN-38': {
                        'AGENT-OF': 'TURN-SWITCH-ON-38',
                        'concept': 'HUMAN',
                        'from-sense': 'SOMEBODY-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [23, [0]],
                        'token': 'Somebody'
                    },
                    'TELEVISION-38': {
                        'THEME-OF': 'TURN-SWITCH-ON-38',
                        'concept': 'TELEVISION',
                        'from-sense':
                        'TELEVISION_SET-N1',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [23, [4]],
                        'token': 'television'
                    },
                    'TURN-SWITCH-ON-38': {
                        'AGENT': 'HUMAN-38',
                        'THEME': 'TELEVISION-38',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'TURN-SWITCH-ON',
                        'from-sense': 'TURN-V4',
                        'is-in-subtree': 'EVENT',
                        'preference': 7.392857,
                        'sem-preference': 4,
                        'sent-word-ind': [23, [1]],
                        'token': 'turned'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 17.39,
                    'semantic-score': 4,
                    'syntactic-score': 15.392857
                },
                'concept_counts': {
                    'HUMAN': {
                        'count': 38,
                        'word-info': [[0, 'top']]
                    },
                    'TELEVISION': {
                        'count': 38,
                        'word-info': [[4, 'top']]
                    },
                    'TURN-SWITCH-ON': {
                        'count': 38,
                        'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['SOMEBODY', 'SOMEBODY-N1', '$VAR0=0', 1],
                    1: ['TURN', 'TURN-V4', '$VAR0=1,$VAR1=0,$VAR2=4,$VAR3=2', 1],
                    4: ['TELEVISION', 'TELEVISION_SET-N1', '$VAR0=4', 1],
                    5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                }
            }
        ],
        'sent-num': 23,
        'sentence': 'Somebody turned on a television.',
        'timestamp': '2020-Mar-22 21:18:39'
    },


    {
        'OriginalSentence': 'Who trained them?',
        'ambiguous-words': {},
        'candidatesBeforePruning': 2,
        'min-maxScores': [12.0, 14.0],
        'results': [
            {
                'TMR': {
                    'HUMAN-39': {
                        'AGENT-OF': 'TRAINING-39',
                        'REQUEST-INFO-TRACE': '+',
                        'concept': 'HUMAN',
                        'from-sense': 'WHO-N1000',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [24, [0]],
                        'token': 'Who'
                    },
                    'SET-39': {
                        'BENEFICIARY-OF': 'TRAINING-39',
                        'CARDINALITY': ['>', 1],
                        'MEMBER-TYPE': 'ALL',
                        'concept': 'SET',
                        'from-sense': 'THEY-N1',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [24, [2]],
                        'token': 'them'
                    },
                    'TRAINING-39': {
                        'AGENT': 'HUMAN-39',
                        'BENEFICIARY': 'SET-39',
                        'TIME': ['<', 'FIND-ANCHOR-TIME'],
                        'concept': 'TRAINING',
                        'from-sense': 'TRAIN-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [24, [1]],
                        'token': 'trained'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 14.0,
                    'semantic-score': 4,
                    'syntactic-score': 12.0
                },
                'concept_counts': {
                    'HUMAN': {
                        'count': 39,
                        'word-info': [[0, 'top']]
                    },
                    'SET': {
                        'count': 39,
                        'word-info': [[2, 'top']]
                    },
                    'TRAINING': {
                        'count': 39,
                        'word-info': [[1, 'top']]
                    }
                },
                'words': {
                    0: ['WHO', 'WHO-N1000', '$VAR0=0,$VAR1=3',1],
                    1: ['TRAIN', 'TRAIN-V1','$VAR0=1,$VAR1=0,$VAR2=2', 1],
                    2: ['THEY', 'THEY-N1', '$VAR0=2', 1]
                }
            }
        ],
        'sent-num': 24,
        'sentence': 'Who trained them?',
        'timestamp': '2020-Mar-22 21:18:39'
    },


    {
        'OriginalSentence': 'We train our agents.',
        'ambiguous-words': {},
        'candidatesBeforePruning': 3,
        'min-maxScores': [8.0, 14.0],
        'results': [
            {
                'TMR': {
                    'HUMAN-40': {
                        'BENEFICIARY-OF': 'TRAINING-40',
                        'CARDINALITY': ['>', 1],
                        'concept': 'HUMAN',
                        'from-sense': 'GENERALIZED-N16',
                        'is-in-subtree': 'OBJECT',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [25, [3]],
                        'token': 'agents'
                    },
                    'SET-40': {
                        'AGENT-OF': 'TRAINING-40',
                        'CARDINALITY': ['>', 1],
                        'MEMBER-TYPE': 'HUMAN',
                        'concept': 'SET',
                        'from-sense': 'WE-N1',
                        'is-in-subtree': 'PROPERTY',
                        'preference': 4.0,
                        'sem-preference': 0,
                        'sent-word-ind': [25, [0]],
                        'token': 'We'
                    },
                    'TRAINING-40': {
                        'AGENT': 'SET-40',
                        'BENEFICIARY': 'HUMAN-40',
                        'TIME': ['FIND-ANCHOR-TIME'],
                        'concept': 'TRAINING',
                        'from-sense': 'TRAIN-V1',
                        'is-in-subtree': 'EVENT',
                        'preference': 4.0,
                        'sem-preference': 4,
                        'sent-word-ind': [25, [1]],
                        'token': 'train'
                    },
                    'baseline-semantic-score': 2,
                    'combined-score': 14.0,
                    'semantic-score': 4,
                    'syntactic-score': 12.0},
                    'concept_counts': {
                        'HUMAN': {
                            'count': 40,
                            'word-info': [[3, 'top']]
                        },
                        'SET': {
                            'count': 40,
                            'word-info': [[0, 'top']]
                        },
                        'TRAINING': {
                            'count': 40,
                            'word-info': [[1, 'top']]
                        }
                    },
                    'words': {
                        0: ['WE', 'WE-N1', '$VAR0=0', 1],
                        1: ['TRAIN', 'TRAIN-V1', '$VAR0=1,$VAR1=0,$VAR2=3', 1],
                        3: ['AGENT', 'GENERALIZED-N16', '$VAR0=3', 1],
                        4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                    }
                }
            ],
            'sent-num': 25,
            'sentence': 'We train our agents.',
            'timestamp': '2020-Mar-22 21:18:39'
        },


        {
            'OriginalSentence': 'Chigurh always tracks him down.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 2,
            'min-maxScores': [12.0, 18.0],
            'results': [
                {
                    'TMR': {
                        'FIND-41': {
                            'AGENT': 'HUMAN-41',
                            'THEME': 'HUMAN-42',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'FIND',
                            'from-sense': 'TRACK-V1',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 4,
                            'sent-word-ind': [26, [2]],
                            'token': 'tracks'
                        },
                        'HUMAN-41': {
                            'AGENT-OF': 'FIND-41',
                            'HAS-PERSONAL-NAME': 'CHIGURH',
                            'concept': 'HUMAN',
                            'from-sense': 'PERSON-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'NER',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [26, [0]],
                            'token': 'Chigurh'
                        },
                        'HUMAN-42': {
                            'GENDER': 'MALE',
                            'THEME-OF': 'FIND-41',
                            'concept': 'HUMAN',
                            'coref': [],
                            'from-sense': 'HE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [26, [3]],
                            'token': 'him'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 18.0,
                        'semantic-score': 4,
                        'syntactic-score': 16.0},
                        'concept_counts': {
                            'FIND': {
                                'count': 41,
                                'word-info': [[2, 'top']]
                            },
                            'HUMAN': {
                                'count': 42,
                                'word-info': [[0, 'top'], [3, 'top']]
                            }
                        },
                        'words': {
                            0: ['CHIGURH', 'PERSON-NAME', '$VAR0=0', 1],
                            1: ['ALWAYS', 'ALWAYS-ADV2', '$VAR0=1,$VAR1=2', 1],
                            2: ['TRACK', 'TRACK-V1', '$VAR0=2,$VAR1=0,$VAR2=4,$VAR3=3', 1],
                            3: ['HE', 'HE-N1', '$VAR0=3', 1],
                            5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                        }
                    }
                ],
                'sent-num': 26,
                'sentence': 'Chigurh always tracks him down.',
                'timestamp': '2020-Mar-22 21:18:39'
            },


            {
                'OriginalSentence': 'I think we found out.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 2,
                'min-maxScores': [20.0, 22.0],
                'results': [
                    {
                        'TMR': {
                            'HUMAN-43': {
                                'ATTRIBUTION': 'MODALITY-43',
                                'concept': 'HUMAN',
                                'from-sense': 'I-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [27, [0]],
                                'token': 'I'
                            },
                            'LEARN-43': {
                                'AGENT': 'SET-43',
                                'SCOPE-OF': 'MODALITY-43',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'LEARN',
                                'from-sense': 'FIND-V7',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 2,
                                'sent-word-ind': [27, [3]],
                                'token': 'found'
                            },
                            'MODALITY-43': {
                                'ATTRIBUTED-TO': 'HUMAN-43',
                                'SCOPE': 'LEARN-43',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'TYPE': 'BELIEF',
                                'VALUE': 0.7,
                                'concept': 'MODALITY',
                                'from-sense': 'THINK-V1',
                                'preference': 4.0,
                                'sem-preference': 2,
                                'sent-word-ind': [27, [1]],
                                'token': 'think'
                            },
                            'SET-43': {
                                'AGENT-OF': 'LEARN-43',
                                'CARDINALITY': ['>', 1],
                                'MEMBER-TYPE': 'HUMAN',
                                'concept': 'SET',
                                'from-sense': 'WE-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [27, [2]],
                                'token': 'we'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 22.0,
                            'semantic-score': 4,
                            'syntactic-score': 20.0
                        },
                        'concept_counts': {
                            'HUMAN': {
                                'count': 43,
                                'word-info': [[0, 'top']]
                            },
                            'LEARN': {
                                'count': 43,
                                'word-info': [[3, 'top']]
                            },
                            'MODALITY': {
                                'count': 43,
                                'word-info': [[1, 'top']]
                            },
                            'SET': {
                                'count': 43,
                                'word-info': [[2, 'top']]
                            }
                        },
                        'words': {
                            0: ['I', 'I-N1', '$VAR0=0', 1],
                            1: ['THINK', 'THINK-V1', '$VAR0=1,$VAR1=0,$VAR2=3', 1],
                            2: ['WE', 'WE-N1', '$VAR0=2', 1],
                            3: ['FIND', 'FIND-V7', '$VAR0=3,$VAR1=2,$VAR2=4,$VAR3=None,$VAR4=None', 1],
                            5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                        }
                    }
                ],
                'sent-num': 27,
                'sentence': 'I think we found out.',
                'timestamp': '2020-Mar-22 21:18:39'
            },



            {
                'OriginalSentence': 'They think about the road.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 2,
                'min-maxScores': [2.0, 18.0],
                'results': [
                    {
                        'TMR': {
                            'ACTIVE-COGNITIVE-EVENT-44': {
                                'AGENT': 'SET-44',
                                'THEME': 'ROAD-44',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'concept': 'ACTIVE-COGNITIVE-EVENT',
                                'from-sense': 'THINK-V6',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 4,
                                'sent-word-ind': [28, [1]],
                                'token': 'think'
                            },
                            'ROAD-44': {
                                'THEME-OF': 'ACTIVE-COGNITIVE-EVENT-44',
                                'concept': 'ROAD',
                                'from-sense': 'ROAD-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [28, [4]],
                                'token': 'road'
                            },
                            'SET-44': {
                                'AGENT-OF': 'ACTIVE-COGNITIVE-EVENT-44',
                                'CARDINALITY': ['>', 1],
                                'MEMBER-TYPE': 'ALL',
                                'concept': 'SET',
                                'from-sense': 'THEY-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [28, [0]],
                                'token': 'They'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 18.0,
                            'semantic-score': 4,
                            'syntactic-score': 16.0
                        },
                        'concept_counts': {
                            'ACTIVE-COGNITIVE-EVENT': {
                                'count':44,
                                'word-info': [[1, 'top']]
                            },
                            'ROAD': {
                                'count': 44,
                                'word-info': [[4, 'top']]
                            },
                            'SET': {
                                'count': 44,
                                'word-info': [[0, 'top']]
                            }
                        },
                        'words': {
                            0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                            1: ['THINK', 'THINK-V6', '$VAR0=1,$VAR1=0,$VAR2=2,$VAR3=4', 1],
                            4: ['ROAD', 'ROAD-N1', '$VAR0=4', 1],
                            5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                        }
                    }
                ],
                'sent-num': 28,
                'sentence': 'They think about the road.',
                'timestamp': '2020-Mar-22 21:18:39'
            },



            {
                'OriginalSentence': 'We stayed for lunch.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 124,
                'min-maxScores': [-18.0, 17.3],
                'results': [
                    {
                        'TMR': {
                            'LUNCH-45': {
                                'PURPOSE-OF': 'REMAIN-45',
                                'concept': 'LUNCH',
                                'from-sense': 'LUNCH-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [29, [3]],
                                'token': 'lunch'
                            },
                            'REMAIN-45': {
                                'PURPOSE': 'LUNCH-45',
                                'THEME': 'SET-45',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'REMAIN',
                                'from-sense': 'STAY-V2',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 4,
                                'sent-word-ind': [29, [1, 2]],
                                'token': 'stayed'
                            },
                            'SET-45': {
                                'CARDINALITY': ['>', 1],
                                'MEMBER-TYPE': 'HUMAN',
                                'THEME-OF': 'REMAIN-45',
                                'concept': 'SET',
                                'from-sense': 'WE-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [29, [0]],
                                'token': 'We'
                            },
                            'baseline-semantic-score': 3,
                            'combined-score': 17.33,
                            'semantic-score': 4,
                            'syntactic-score': 16.0
                        },
                        'concept_counts': {
                            'LUNCH': {
                                'count': 45,
                                'word-info': [[3, 'top']]
                            },
                            'REMAIN': {
                                'count': 45,
                                'word-info': [[1, 'top']]
                            },
                            'SET': {
                                'count': 45,
                                'word-info': [[0, 'top']]
                            }
                        },
                        'words': {
                            0: ['WE', 'WE-N1', '$VAR0=0', 1],
                            1: ['STAY', 'STAY-V2', '$VAR0=1,$VAR1=0', 1],
                            2: ['FOR', 'FOR-PREP2', '$VAR0=2,$VAR1=1,$VAR2=3', 1],
                            3: ['LUNCH', 'LUNCH-N1', '$VAR0=3', 1],
                            4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                        }
                    }
                ],
                'sent-num': 29,
                'sentence': 'We stayed for lunch.',
                'timestamp': '2020-Mar-22 21:18:39'
            },



            {
                'OriginalSentence': 'Joseph would stay there forever.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 2,
                'min-maxScores': [13.7, 17.7],
                'results': [
                    {
                        'TMR': {
                            'HUMAN-46': {
                                'GENDER': 'MALE',
                                'HAS-PERSONAL-NAME': 'JOSEPH',
                                'THEME-OF': 'REMAIN-46',
                                'concept': 'HUMAN',
                                'from-sense': 'PERSON-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'NER',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [30, [0]],
                                'token': 'Joseph'
                            },
                            'LOCATION-46': {
                                'DOMAIN': 'REMAIN-46',
                                'RANGE': 'PLACE-46',
                                'concept': 'LOCATION',
                                'from-sense': 'THERE-ADV1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 2,
                                'sent-word-ind': [30, [3]],
                                'token': 'there'
                            },
                            'PLACE-46': {
                                'RANGE-OF': 'LOCATION-46',
                                'concept': 'PLACE',
                                'from-refsem': 'REFSEM1',
                                'from-sense': 'THERE-ADV1',
                                'sem-preference': 0,
                                'sent-word-ind': [30, [3]],
                                'token': 'there'
                            },
                            'REMAIN-46': {
                                'DOMAIN-OF': 'LOCATION-46',
                                'THEME': 'HUMAN-46',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'TIME-END': '*NOTHING*',
                                'concept': 'REMAIN',
                                'from-sense': 'STAY-V2',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 3,
                                'sent-word-ind': [30, [2, 4]],
                                'token': 'stay'
                            },
                            'baseline-semantic-score': 3,
                            'combined-score': 17.67,
                            'semantic-score': 5,
                            'syntactic-score': 16.0
                        },
                        'concept_counts': {
                            'HUMAN': {
                                'count': 46,
                                'word-info': [[0, 'top']]
                            },
                            'LOCATION': {
                                'count': 46,
                                'word-info': [[3, 'top']]
                            },
                            'PLACE': {
                                'count': 46,
                                'word-info': [[1001, 'top']]
                            },
                            'REMAIN': {
                                'count': 46,
                                'word-info': [[2, 'top']]
                            }
                        },
                        'words': {
                            0: ['JOSEPH', 'PERSON-NAME', '$VAR0=0', 1],
                            1: ['WOULD', 'WOULD-AUX1', '$VAR0=1,$VAR1=2', 1],
                            2: ['STAY', 'STAY-V2', '$VAR0=2,$VAR1=0', 1],
                            3: ['THERE', 'THERE-ADV1', '$VAR0=3,$VAR1=2', 1],
                            4: ['FOREVER', 'FOREVER-ADV1', '$VAR0=4,$VAR1=2', 1],
                            5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                        }
                    }
                ],
                'sent-num': 30,
                'sentence': 'Joseph would stay there forever.',
                'timestamp': '2020-Mar-22 21:18:39'
            },



            {
                'OriginalSentence': 'Maeda had stood up for Mosley.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 3736,
                'min-maxScores': [-6.0, 26.0],
                'results': [
                    {
                        'TMR': {
                            'ASPECT-47': {
                                'PHASE': 'END',
                                'SCOPE': 'PROTECT-47',
                                'concept': 'ASPECT',
                                'from-sense': 'HAVE-AUX3',
                                'sem-preference': 0,
                                'sent-word-ind': [31, [1]],
                                'token': 'had'
                            },
                            'HUMAN-47': {
                                'AGENT-OF': 'PROTECT-47',
                                'HAS-PERSONAL-NAME': 'MAEDA',
                                'concept': 'HUMAN',
                                'from-sense': 'PERSON-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'NER',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [31, [0]],
                                'token': 'Maeda'
                            },
                            'HUMAN-48': {
                                'HAS-PERSONAL-NAME': 'MOSLEY',
                                'THEME-OF': 'PROTECT-47',
                                'concept': 'HUMAN',
                                'from-sense': 'PERSON-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'NER',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [31, [5]],
                                'token': 'Mosley'
                            },
                            'PROTECT-47': {
                                'AGENT': 'HUMAN-47',
                                'SCOPE-OF': 'ASPECT-47',
                                'THEME': 'HUMAN-48',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'PROTECT',
                                'from-sense': 'STAND-V7',
                                'is-in-subtree': 'EVENT',
                                'preference': 16.0,
                                'sem-preference': 4,
                                'sent-word-ind': [31, [2, 1]],
                                'token': 'stood'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 26.0,
                            'semantic-score': 4,
                            'syntactic-score': 24.0
                        },
                        'concept_counts': {
                            'ASPECT': {
                                'count': 48,
                                'word-info': [[1, 'top'], [2, 'top']]
                            },
                            'HUMAN': {
                                'count': 48,
                                'word-info': [[0, 'top'], [5, 'top']]
                            },
                            'PROTECT': {
                                'count': 47,
                                'word-info': [[2, 'top']]
                            }
                        },
                        'words': {
                            0: ['MAEDA', 'PERSON-NAME', '$VAR0=0', 1],
                            1: ['HAVE', 'HAVE-AUX3', '$VAR0=1,$VAR1=2', 1],
                            2: ['STAND', 'STAND-V7', '$VAR0=2,$VAR1=0,$VAR2=3,$VAR3=5,$VAR5=4', 1],
                            5: ['MOSLEY', 'PERSON-NAME', '$VAR0=5', 1],
                            6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                        }
                    }
                ],
                'sent-num': 31,
                'sentence': 'Maeda had stood up for Mosley.',
                'timestamp': '2020-Mar-22 21:18:46'
            },



            {
                'OriginalSentence': 'They speed up.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 3,
                'min-maxScores': [8.0, 14.0],
                'results': [
                    {
                        'TMR': {
                            'CHANGE-EVENT-49': {
                                'EFFECT': 'VELOCITY-50',
                                'PRECONDITION':
                                'VELOCITY-49',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'concept': 'CHANGE-EVENT',
                                'from-sense': 'SPEED-V1',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 0,
                                'sent-word-ind': [32, [1]],
                                'token': 'speed'
                            },
                            'SET-49': {
                                'CARDINALITY': ['>', 1],
                                'DOMAIN-OF': 'VELOCITY-49',
                                'DOMAIN-OF-1': 'VELOCITY-50',
                                'MEMBER-TYPE': 'ALL',
                                'concept': 'SET',
                                'from-sense': 'THEY-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [32, [0]],
                                'token': 'They'
                            },
                            'VELOCITY-49': {
                                'DOMAIN': 'SET-49',
                                'PRECONDITION-OF': 'CHANGE-EVENT-49',
                                'RANGE': ['<',
                                'VELOCITY-50.RANGE'],
                                'concept': 'VELOCITY',
                                'from-refsem': 'REFSEM1',
                                'from-sense': 'SPEED-V1',
                                'sem-preference': 2,
                                'sent-word-ind': [32, [1]],
                                'token': 'speed'
                            },
                            'VELOCITY-50': {
                                'CAUSED-BY': 'CHANGE-EVENT-49',
                                'DOMAIN': 'SET-49',
                                'RANGE': ['>',
                                'VELOCITY-49.RANGE'],
                                'concept': 'VELOCITY',
                                'from-refsem': 'REFSEM2',
                                'from-sense': 'SPEED-V1',
                                'sem-preference': 2,
                                'sent-word-ind': [32, [1]],
                                'token': 'speed'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 14.0,
                            'semantic-score': 4,
                            'syntactic-score': 12.0
                        },
                        'concept_counts': {
                            'CHANGE-EVENT': {
                                'count': 49,
                                'word-info': [[1, 'top']]
                            },
                            'SET': {
                                'count': 49,
                                'word-info': [[0, 'top']]
                            },
                            'VELOCITY': {
                                'count': 50,
                                'word-info': [[1001, 'top'], [1002, 'top']]
                            }
                        },
                        'words': {
                            0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                            1: ['SPEED', 'SPEED-V1', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                            3: ['.', '.-PUNCT1', '$VAR0=3', 1]
                        }
                    }
                ],
                'sent-num': 32,
                'sentence': 'They speed up.',
                'timestamp': '2020-Mar-22 21:18:46'
            },



            {
                'OriginalSentence': 'The courts must sign off on any final accounting.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 32,
                'min-maxScores': [18.0, 34.0],
                'results': [
                    {
                        'TMR': {
                            'ACCOUNTING-51': {
                                'ELEMENTS-OF': 'SET-52',
                                'concept': 'ACCOUNTING',
                                'from-sense': 'ACCOUNTING-N1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [33, [8]],
                                'token': 'accounting'
                            },
                            'APPROVE-51': {
                                'AGENT': 'COURT-51',
                                'SCOPE-OF': 'MODALITY-51',
                                'THEME': 'SET-52',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'concept': 'APPROVE',
                                'from-sense': 'SIGN-V7',
                                'is-in-subtree': 'EVENT',
                                'preference': 12.0,
                                'sem-preference': 4,
                                'sent-word-ind': [33, [3]],
                                'token': 'sign'
                            },
                            'COURT-51': {
                                'AGENT-OF': 'APPROVE-51',
                                'CARDINALITY': ['>', 1],
                                'concept': 'COURT',
                                'from-sense': 'COURT-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [33, [1]],
                                'token': 'courts'
                            },
                            'MODALITY-51': {
                                'SCOPE': 'APPROVE-51',
                                'TYPE': 'OBLIGATIVE',
                                'VALUE': 1,
                                'concept': 'MODALITY',
                                'from-sense': 'MUST-AUX1',
                                'preference': 4.0,
                                'sem-preference': 2,
                                'sent-word-ind': [33, [2]],
                                'token': 'must'
                            },
                            'SET-51': {
                                'CARDINALITY': 1,
                                'DETERMINATE': 'NO',
                                'MEMBER-TYPE': 'SET-52',
                                'concept': 'SET',
                                'from-sense': 'ANY-DET1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 2,
                                'sent-word-ind': [33, [6]],
                                'token': 'any'
                            },
                            'SET-52': {
                                'CARDINALITY': 1,
                                'COMPLETE': 'NO',
                                'ELEMENTS': ['ACCOUNTING-51'],
                                'MEMBER-TYPE-OF': 'SET-51',
                                'THEME-OF': 'APPROVE-51',
                                'concept': 'SET',
                                'from-sense': 'LAST-ADJ3',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [33, [7]],
                                'token': 'final'
                            },
                            'baseline-semantic-score': 4,
                            'combined-score': 34.0,
                            'semantic-score': 8,
                            'syntactic-score': 32.0
                        },
                        'concept_counts': {
                            'ACCOUNTING': {
                                'count': 51,
                                'word-info': [[8, 'top']]
                            },
                            'APPROVE': {
                                'count': 51,
                                'word-info': [[3, 'top']]
                            },
                            'COURT': {
                                'count': 51,
                                'word-info': [[1, 'top']]
                            },
                            'MODALITY': {
                                'count': 51,
                                'word-info': [[2, 'top']]
                            },
                            'SET': {
                                'count': 52,
                                'word-info': [[6, 'top'], [7, 'top']]
                            }
                        },
                        'words': {
                            1: ['COURT', 'COURT-N1', '$VAR0=1', 1],
                            2: ['MUST', 'MUST-AUX1', '$VAR0=2,$VAR1=1,$VAR2=3', 1],
                            3: ['SIGN', 'SIGN-V7', '$VAR0=3,$VAR1=1,$VAR2=4,$VAR3=5,$VAR4=8', 1],
                            6: ['ANY', 'ANY-DET1', '$VAR0=6,$VAR1=8', 1],
                            7: ['FINAL', 'LAST-ADJ3', '$VAR0=7,$VAR2=8', 1],
                            8: ['ACCOUNTING', 'ACCOUNTING-N1', '$VAR0=8', 1],
                            9: ['.', '.-PUNCT1', '$VAR0=9', 1]
                        }
                    }
                ],
                'sent-num': 33,
                'sentence': 'The courts must sign off on any final accounting.',
                'timestamp': '2020-Mar-22 21:18:46'
            },


            {
                'OriginalSentence': 'He showered.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 1,
                'min-maxScores': [10.0, 10.0],
                'results': [
                    {
                        'TMR': {
                            'BATHE-HUMAN-53': {
                                'AGENT': 'HUMAN-53',
                                'INSTRUMENT': 'SHOWER',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'BATHE-HUMAN',
                                'from-sense': 'SHOWER-V1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 2,
                                'sent-word-ind': [34, [1]],
                                'token': 'showered'
                            },
                            'HUMAN-53': {
                                'AGENT-OF': 'BATHE-HUMAN-53',
                                'GENDER': 'MALE',
                                'concept': 'HUMAN',
                                'from-sense': 'HE-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [34, [0]],
                                'token': 'He'
                            },
                            'baseline-semantic-score': 1,
                            'combined-score': 10.0,
                            'semantic-score': 2,
                            'syntactic-score': 8.0
                        },
                        'concept_counts': {
                            'BATHE-HUMAN': {
                                'count': 53,
                                'word-info': [[1, 'top']]
                            },
                            'HUMAN': {
                                'count': 53,
                                'word-info': [[0,'top']]
                            }
                        },
                        'words': {
                            0: ['HE', 'HE-N1', '$VAR0=0', 1],
                        1: ['SHOWER', 'SHOWER-V1', '$VAR0=1,$VAR1=0', 1],
                        2: ['.', '.-PUNCT1', '$VAR0=2', 1]
                    }
                }
            ],
            'sent-num': 34,
            'sentence': 'He showered.',
            'timestamp': '2020-Mar-22 21:18:46'
        },


        {
            'OriginalSentence': 'Nobody had shot back at them.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 6,
            'min-maxScores': [20.2, 26.0],
            'results': [
                {
                    'TMR': {
                        'ASPECT-54': {
                            'PHASE': 'END',
                            'SCOPE': 'DISCHARGE-WEAPON-54',
                            'concept': 'ASPECT',
                            'from-sense': 'HAVE-AUX3',
                            'sem-preference': 0,
                            'sent-word-ind': [35, [1]],
                            'token': 'had'
                        },
                        'DISCHARGE-WEAPON-54': {
                            'AGENT': 'SET-54',
                            'DESTINATION': 'SET-55',
                            'EFFECT': 'RETURN',
                            'SCOPE-OF': 'ASPECT-54',
                            'SCOPE-OF-1': 'MODALITY-54',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'DISCHARGE-WEAPON',
                            'from-sense': 'SHOOT-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 16.0,
                            'sem-preference': 6,
                            'sent-word-ind': [35, [2, 1, 3]],
                            'token': 'shot'
                        },
                        'MODALITY-54': {
                            'SCOPE': 'DISCHARGE-WEAPON-54',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'TYPE': 'EPITEUCTIC',
                            'VALUE': 0,
                            'concept': 'MODALITY',
                            'from-sense': 'SHOOT-V2',
                            'sem-preference': 0,
                            'sent-word-ind': [35, [2]],
                            'token': 'shot'
                        },
                        'SET-54': {
                            'AGENT-OF': 'DISCHARGE-WEAPON-54',
                            'CARDINALITY': 0,
                            'COMPLETE': 'YES',
                            'MEMBER-TYPE': 'HUMAN',
                            'concept': 'SET',
                            'from-sense': 'NO_ONE-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [35, [0]],
                            'token': 'Nobody'
                        },
                        'SET-55': {
                            'CARDINALITY': ['>', 1],
                            'DESTINATION-OF': 'DISCHARGE-WEAPON-54',
                            'MEMBER-TYPE': 'ALL',
                            'concept': 'SET',
                            'from-sense': 'THEY-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [35, [5]],
                            'token': 'them'
                        },
                        'baseline-semantic-score': 3,
                        'combined-score': 26.0,
                        'semantic-score': 6,
                        'syntactic-score': 24.0
                    },
                    'concept_counts': {
                        'ASPECT': {
                            'count': 54,
                            'word-info': [[1, 'top']]
                        },
                        'DISCHARGE-WEAPON': {
                            'count': 54,
                            'word-info': [[2, 'top']]
                        },
                        'MODALITY': {
                            'count': 54,
                            'word-info': [[2, 'top']]
                        },
                        'SET': {
                            'count': 55,
                            'word-info': [[0, 'top'], [5, 'top']]
                        }
                    },
                    'words': {
                        0: ['NOBODY', 'NO_ONE-N1', '$VAR0=0', 1],
                        1: ['HAVE', 'HAVE-AUX3', '$VAR0=1,$VAR1=2', 1],
                        2: ['SHOOT', 'SHOOT-V2', '$VAR0=2,$VAR1=0,$VAR2=None,$VAR3=4,$VAR4=5', 1],
                        3: ['BACK', 'BACK-ADV1', '$VAR0=3,$VAR1=2', 1],
                        5: ['THEY', 'THEY-N1', '$VAR0=5', 1],
                        6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                    }
                }
            ],
            'sent-num': 35,
            'sentence': 'Nobody had shot back at them.',
            'timestamp': '2020-Mar-22 21:18:46'
        },



        {
            'OriginalSentence': 'They share lab space.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 2,
            'min-maxScores': [18.0, 18.0],
            'results': [
                {
                    'TMR': {
                        'LABORATORY-56': {
                            'DOMAIN-OF': 'RELATION-56',
                            'concept': 'LABORATORY',
                            'from-sense': 'LABORATORY-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [36, [2]],
                            'token': 'lab'
                        },
                        'RELATION-56': {
                            'DOMAIN': 'LABORATORY-56',
                            'RANGE': 'SPACE-56',
                            'concept': 'RELATION',
                            'is-in-subtree': 'PROPERTY',
                            'sem-preference': 0
                        },
                        'SET-56': {
                            'AGENT-OF': 'SHARE-EVENT-56',
                            'CARDINALITY': ['>', 1],
                            'MEMBER-TYPE': 'ALL',
                            'concept': 'SET',
                            'from-sense': 'THEY-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [36, [0]],
                            'token': 'They'
                        },
                        'SHARE-EVENT-56': {
                            'AGENT': 'SET-56',
                            'THEME': 'SPACE-56',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'SHARE-EVENT',
                            'from-sense': 'SHARE-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 4,
                            'sent-word-ind': [36, [1]],
                            'token': 'share'
                        },
                        'SPACE-56': {
                            'RANGE-OF': 'RELATION-56',
                            'THEME-OF': 'SHARE-EVENT-56',
                            'concept': 'SPACE',
                            'from-sense': 'SPACE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [36, [3]],
                            'token': 'space'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 18.0,
                        'semantic-score': 4,
                        'syntactic-score': 16.0},
                        'concept_counts': {
                            'LABORATORY': {
                                'count': 56,
                                'word-info': [[2, 'top']]
                            },
                            'SET': {
                                'count': 56,
                                'word-info': [[0, 'top']]
                            },
                            'SHARE-EVENT': {
                                'count': 56,
                                'word-info': [[1, 'top']]
                            },
                            'SPACE': {
                                'count': 56,
                                'word-info': [[3, 'top']]
                            }
                        },
                        'words': {
                            0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                            1: ['SHARE', 'SHARE-V2', '$VAR0=1,$VAR1=0,$VAR2=3', 1],
                            2: ['LAB', 'LABORATORY-N1', '$VAR0=2', 1],
                            3: ['SPACE', 'SPACE-N1', '$VAR0=3', 1],
                            4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                        }
                    }
                ],
                'sent-num': 36,
                'sentence': 'They share lab space.',
                'timestamp': '2020-Mar-22 21:18:46'
            },


            {
                'OriginalSentence': 'They would shape policy.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 6,
                'min-maxScores': [-1.0, 14.0],
                'results': [
                    {
                        'TMR': {
                            'CHANGE-EVENT-57': {
                                'AGENT': 'SET-57',
                                'THEME': 'PROCEDURE-57',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'concept': 'CHANGE-EVENT',
                                'from-sense': 'SHAPE-V1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 4,
                                'sent-word-ind': [37, [2]],
                                'token': 'shape'
                            },
                            'MODALITY-57': {
                                'SCOPE': 'PROCEDURE-57',
                                'TYPE': 'OBLIGATIVE',
                                'VALUE': 0.7,
                                'concept': 'MODALITY',
                                'from-sense': 'POLICY-N1',
                                'sem-preference': 0,
                                'sent-word-ind': [37, [3]],
                                'token': 'policy'
                            },
                            'PROCEDURE-57': {
                                'FORMALITY': 0.7,
                                'SCOPE-OF': 'MODALITY-57',
                                'THEME-OF': 'CHANGE-EVENT-57',
                                'concept': 'PROCEDURE',
                                'from-sense': 'POLICY-N1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [37, [3]],
                                'token': 'policy'
                            },
                            'SET-57': {
                                'AGENT-OF': 'CHANGE-EVENT-57',
                                'CARDINALITY': ['>', 1],
                                'MEMBER-TYPE': 'ALL',
                                'concept': 'SET',
                                'from-sense': 'THEY-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [37, [0]],
                                'token': 'They'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 14.0,
                            'semantic-score': 4,
                            'syntactic-score': 12.0
                        },
                        'concept_counts': {
                            'CHANGE-EVENT': {
                                'count': 57,
                                'word-info': [[2, 'top']]
                            },
                            'MODALITY': {
                                'count': 57,
                                'word-info': [[3, 'top']]
                            },
                            'PROCEDURE': {
                                'count': 57,
                                'word-info': [[3, 'top']]
                            },
                            'SET': {
                                'count': 58,
                                'word-info': [[0, 'top'], [1002, 'top']]
                            }
                        },
                        'words': {
                            0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                            1: ['WOULD', 'WOULD-AUX1', '$VAR0=1,$VAR1=2', 1],
                            2: ['SHAPE', 'SHAPE-V1', '$VAR0=2,$VAR1=0,$VAR2=3', 1],
                            3: ['POLICY', 'POLICY-N1', '$VAR0=3,$VAR1=None,$VAR2=None', 1],
                            4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                        }
                    }
                ],
                'sent-num': 37,
                'sentence': 'They would shape policy.',
                'timestamp': '2020-Mar-22 21:18:46'
            },


            {
                'OriginalSentence': 'They settled in Minsk.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 21,
                'min-maxScores': [6.0, 18.5],
                'results': [
                    {
                        'TMR': {
                            'ASPECT-59': {
                                'PHASE': 'BEGIN',
                                'SCOPE': 'INHABIT-59',
                                'concept': 'ASPECT',
                                'from-sense': 'SETTLE-V3',
                                'sem-preference': 0,
                                'sent-word-ind': [38, [1]],
                                'token': 'settled'
                            },
                            'CITY-59': {
                                'HAS-NAME': 'MINSK',
                                'LOCATION-OF': 'INHABIT-59',
                                'concept': 'CITY',
                                'from-sense': 'OTHER-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'onomasticon',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [38, [3]],
                                'token': 'Minsk'
                            },
                            'INHABIT-59': {
                                'AGENT': 'SET-59',
                                'LOCATION': 'CITY-59',
                                'SCOPE-OF': 'ASPECT-59',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'INHABIT',
                                'from-sense': 'SETTLE-V3',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 5,
                                'sent-word-ind': [38, [1]],
                                'token': 'settled'
                            },
                            'SET-59': {
                                'AGENT-OF': 'INHABIT-59',
                                'CARDINALITY': ['>', 1],
                                'MEMBER-TYPE': 'ALL',
                                'concept': 'SET',
                                'from-sense': 'THEY-N1',
                                'is-in-subtree': 'PROPERTY',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [38, [0]],
                                'token': 'They'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 18.5,
                            'semantic-score': 5,
                            'syntactic-score': 16.0
                        },
                        'concept_counts': {
                            'ASPECT': {
                                'count': 59,
                                'word-info': [[1, 'top']]
                            },
                            'CITY': {
                                'count': 59,
                                'word-info': [[3, 'top']]
                            },
                            'INHABIT': {
                                'count': 59,
                                'word-info': [[1, 'top']]
                            },
                            'SET': {
                                'count': 59,
                                'word-info': [[0, 'top']]
                            }
                        },
                        'words': {
                            0: ['THEY', 'THEY-N1', '$VAR0=0', 1],
                            1: ['SETTLE', 'SETTLE-V3', '$VAR0=1,$VAR1=0,$VAR2=2,$VAR3=3', 1],
                            3: ['MINSK', 'OTHER-NAME', '$VAR0=3', 1],
                            4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                        }
                    }
                ],
                'sent-num': 38,
                'sentence': 'They settled in Minsk.',
                'timestamp': '2020-Mar-22 21:18:46'
            },


            {
                'OriginalSentence': "He'll never send the money.",
                'ambiguous-words': {},
                'candidatesBeforePruning': 1,
                'min-maxScores': [18.0, 18.0],
                'results': [
                    {
                        'TMR': {
                            'HUMAN-60': {
                                'AGENT-OF': 'SEND-60',
                                'GENDER': 'MALE',
                                'concept': 'HUMAN',
                                'from-sense': 'HE-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [39, [0]],
                                'token': 'He'
                            },
                            'MODALITY-60': {
                                'SCOPE': 'SEND-60',
                                'TYPE': 'EPISTEMIC',
                                'VALUE': 0,
                                'concept': 'MODALITY',
                                'from-sense': 'NEVER-ADV1',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [39, [2]],
                                'token': 'never'
                            },
                            'MONEY-60': {
                                'THEME-OF': 'SEND-60',
                                'concept': 'MONEY',
                                'from-sense': 'MONEY-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [39, [5]],
                                'token': 'money'
                            },
                            'SEND-60': {
                                'AGENT': 'HUMAN-60',
                                'SCOPE-OF': 'MODALITY-60',
                                'THEME': 'MONEY-60',
                                'TIME': ['>', 'FIND-ANCHOR-TIME'],
                                'concept': 'SEND',
                                'from-sense': 'SEND-V2',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 4,
                                'sent-word-ind': [39, [3]],
                                'token': 'send'
                            },
                            'baseline-semantic-score': 2,
                            'combined-score': 18.0,
                            'semantic-score': 4,
                            'syntactic-score': 16.0
                        },
                        'concept_counts': {
                            'DESTINATION': {
                                'count': 60,
                                'word-info': [[1001, 'top']]
                            },
                            'HUMAN': {
                                'count': 60,
                                'word-info': [[0, 'top']]
                            },
                            'MODALITY': {
                                'count': 60,
                                'word-info': [[2, 'top']]
                            },
                            'MONEY': {
                                'count': 60,
                                'word-info': [[5, 'top']]
                            },
                            'SEND': {
                                'count': 60,
                                'word-info': [[3, 'top']]
                            }
                        },
                        'words': {
                            0: ['HE', 'HE-N1', '$VAR0=0', 1],
                            1: ['WILL', 'WILL-AUX1', '$VAR0=1,$VAR1=3', 1],
                            2: ['NEVER', 'NEVER-ADV1', '$VAR0=2,$VAR1=3', 1],
                            3: ['SEND', 'SEND-V2', '$VAR0=3,$VAR1=0,$VAR2=5,$VAR3=None,$VAR4=None', 1],
                            5: ['MONEY', 'MONEY-N1', '$VAR0=5', 1],
                            6: ['.', '.-PUNCT1', '$VAR0=6', 1]
                        }
                    }
                ],
                'sent-num': 39,
                'sentence': "He'll never send the money.",
                'timestamp': '2020-Mar-22 21:18:46'
            },



            {
                'OriginalSentence': "I'll see you on the freeway.",
                'ambiguous-words': {},
                'candidatesBeforePruning': 4,
                'min-maxScores': [18.5, 21.5],
                'results': [
                    {
                        'TMR': {
                            'HIGHWAY-61': {
                                'PATH-OF': 'VISUAL-EVENT-61',
                                'concept': 'HIGHWAY',
                                'from-sense': 'FREEWAY-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [40, [6]],
                                'token': 'freeway'
                            },
                            'HUMAN-61': {
                                'EXPERIENCER-OF': 'VISUAL-EVENT-61',
                                'concept': 'HUMAN',
                                'from-sense': 'I-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [40, [0]],
                                'token': 'I'
                            },
                            'HUMAN-62': {
                                'THEME-OF': 'VISUAL-EVENT-61',
                                'concept': 'HUMAN',
                                'from-sense': 'YOU-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [40, [3]],
                                'token': 'you'
                            },
                            'VISUAL-EVENT-61': {
                                'EXPERIENCER': 'HUMAN-61',
                                'PATH': 'HIGHWAY-61',
                                'THEME': 'HUMAN-62',
                                'TIME': ['FIND-ANCHOR-TIME'],
                                'concept': 'VISUAL-EVENT',
                                'from-sense': 'SEE-V1',
                                'is-in-subtree': 'EVENT',
                                'preference': 8.0,
                                'sem-preference': 6,
                                'sent-word-ind': [40, [2,4]],
                                'token': 'see'
                            },
                            'baseline-semantic-score': 4,
                            'combined-score': 21.5,
                            'semantic-score': 6,
                            'syntactic-score': 20.0
                        },
                        'concept_counts': {
                            'HIGHWAY': {
                                'count': 61,
                                'word-info': [[6, 'top']]
                            },
                            'HUMAN': {
                                'count': 62,
                                'word-info': [[0, 'top'], [3, 'top']]
                            },
                            'VISUAL-EVENT': {
                                'count': 61,
                                'word-info': [[2, 'top']]
                            }
                        },
                        'words': {
                            0: ['I', 'I-N1', '$VAR0=0', 1],
                            1: ['WILL', 'WILL-AUX1', '$VAR0=1,$VAR1=2', 1],
                            2: ['SEE', 'SEE-V1', '$VAR0=2,$VAR1=0,$VAR2=3', 1],
                            3: ['YOU', 'YOU-N1', '$VAR0=3', 1],
                            4: ['ON', 'ON-PREP13', '$VAR0=4,$VAR1=2,$VAR2=6', 1],
                            6: ['FREEWAY', 'FREEWAY-N1', '$VAR0=6', 1],
                            7: ['.', '.-PUNCT1', '$VAR0=7', 1]
                        }
                    }
                ],
                'sent-num': 40,
                'sentence': "I'll see you on the freeway.",
                'timestamp': '2020-Mar-22 21:18:46'
            },


            {
                'OriginalSentence': 'She saw an injured Graves at the cafeteria door.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 32,
                'min-maxScores': [18.8, 29.3],
                'results': [
                    {
                        'TMR': {
                            'CAFETERIA-63': {
                                'DOMAIN-OF': 'RELATION-63',
                                'concept': 'CAFETERIA',
                                'from-sense': 'CAFETERIA-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [41, [7]],
                                'token': 'cafeteria'
                            },
                            'DOOR-63': {
                                'LOCATION-OF': 'VISUAL-EVENT-63',
                                'RANGE-OF': 'RELATION-63',
                                'concept': 'DOOR',
                                'from-sense': 'DOOR-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [41, [8]],
                                'token': 'door'
                            },
                            'HUMAN-63': {
                                'EXPERIENCER-OF': 'VISUAL-EVENT-63',
                                'GENDER': 'FEMALE',
                                'concept': 'HUMAN',
                                'from-sense': 'SHE-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [41, [0]],
                                'token': 'She'
                            },
                            'HUMAN-64': {
                                'BENEFICIARY-OF': 'INJURY',
                                'HAS-PERSONAL-NAME': 'GRAVES',
                                'THEME-OF': 'VISUAL-EVENT-63',
                                'concept': 'HUMAN',
                                'from-sense': 'PERSON-NAME',
                                'is-in-subtree': 'OBJECT',
                                'lex-source': 'NER',
                                'preference': 8.0,
                                'sem-preference': 1,
                                'sent-word-ind': [41, [4, 3]],
                                'token': 'Graves'
                            },
                            'RELATION-63': {
                                'DOMAIN': 'CAFETERIA-63',
                                'RANGE': 'DOOR-63',
                                'concept': 'RELATION',
                                'is-in-subtree': 'PROPERTY',
                                'sem-preference': 0
                            },
                            'VISUAL-EVENT-63': {
                                'EXPERIENCER': 'HUMAN-63',
                                'LOCATION': 'DOOR-63',
                                'THEME': 'HUMAN-64',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'VISUAL-EVENT',
                                'from-sense': 'SEE-V1',
                                'is-in-subtree': 'EVENT',
                                'preference': 7.5,
                                'sem-preference': 8,
                                'sent-word-ind': [41, [1,5]],
                                'token': 'saw'
                            },
                            'baseline-semantic-score': 5,
                            'combined-score': 29.3,
                            'semantic-score': 9,
                            'syntactic-score': 27.5
                        },
                        'concept_counts': {
                            'CAFETERIA': {
                                'count': 63,
                                'word-info': [[7, 'top']]
                            },
                            'DOOR': {
                                'count': 63,
                                'word-info': [[8, 'top']]
                            },
                            'HUMAN': {
                                'count': 64,
                                'word-info': [[0, 'top'], [4, 'top']]
                            },
                            'VISUAL-EVENT': {
                                'count': 63,
                                'word-info': [[1, 'top']]
                            }
                        },
                        'words': {
                            0: ['SHE', 'SHE-N1', '$VAR0=0', 1],
                            1: ['SEE', 'SEE-V1', '$VAR0=1,$VAR1=0,$VAR2=4', 1],
                            3: ['INJURED', 'INJURED-ADJ2', '$VAR0=3,$VAR1=4', 1],
                            4: ['GRAVES', 'PERSON-NAME', '$VAR0=4', 1],
                            5: ['AT', 'AT-PREP1', '$VAR0=5,$VAR1=1,$VAR2=8', 2],
                            7: ['CAFETERIA', 'CAFETERIA-N1', '$VAR0=7', 1],
                            8: ['DOOR', 'DOOR-N1', '$VAR0=8', 1],
                            9: ['.', '.-PUNCT1', '$VAR0=9', 1]
                        }
                    }
                ],
                'sent-num': 41,
                'sentence': 'She saw an injured Graves at the cafeteria door.',
                'timestamp': '2020-Mar-22 21:18:46'
            },



            {
                'OriginalSentence': 'Legislators scheduled hearings.',
                'ambiguous-words': {},
                'candidatesBeforePruning': 1,
                'min-maxScores': [14.0, 14.0],
                'results': [
                    {
                        'TMR': {
                            'HEARING-65': {
                                'CARDINALITY': ['>', 1],
                                'THEME-OF': 'SCHEDULE-EVENT-65',
                                'concept': 'HEARING',
                                'from-sense': 'HEARING-N1',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [42, [2]],
                                'token': 'hearings'
                            },
                            'POLITICIAN-65': {
                                'AGENT-OF': 'SCHEDULE-EVENT-65',
                                'CARDINALITY': ['>', 1],
                                'MEMBER-OF': 'LEGISLATIVE-ENTITY',
                                'concept': 'POLITICIAN',
                                'from-sense': 'LEGISLATOR-N1',
                                'is-in-subtree': 'OBJECT',
                                'preference': 4.0,
                                'sem-preference': 0,
                                'sent-word-ind': [42, [0]],
                                'token': 'Legislators'
                            },
                            'SCHEDULE-EVENT-65': {
                                'AGENT': 'POLITICIAN-65',
                                'THEME': 'HEARING-65',
                                'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                'concept': 'SCHEDULE-EVENT',
                                'from-sense': 'SCHEDULE-V2',
                                'is-in-subtree': 'EVENT',
                                'preference': 4.0,
                                'sem-preference': 4,
                                'sent-word-ind': [42,[1]],
                                'token': 'scheduled'},
                                'baseline-semantic-score': 2,
                                'combined-score': 14.0,
                                'semantic-score': 4,
                                'syntactic-score': 12.0
                            },
                            'concept_counts': {
                                'HEARING': {
                                    'count': 65, 'word-info': [[2, 'top']]
                                },
                                'POLITICIAN': {
                                    'count': 65, 'word-info': [[0, 'top']]
                                },
                                'SCHEDULE-EVENT': {
                                    'count': 65,
                                    'word-info': [[1, 'top']]
                                }
                            },
                            'words': {
                                0: ['LEGISLATOR', 'LEGISLATOR-N1', '$VAR0=0', 1],
                                1: ['SCHEDULE', 'SCHEDULE-V2', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                                2: ['HEARING', 'HEARING-N1', '$VAR0=2', 1],
                                3: ['.', '.-PUNCT1', '$VAR0=3', 1]
                            }
                        }
                    ],
                    'sent-num': 42,
                    'sentence': 'Legislators scheduled hearings.',
                    'timestamp': '2020-Mar-22 21:18:46'
                },


                {
                    'OriginalSentence': 'I ran to the door.',
                    'ambiguous-words': {},
                    'candidatesBeforePruning': 12,
                    'min-maxScores': [-10.0, 16.0],
                    'results': [
                        {
                            'TMR': {
                                'DOOR-66': {
                                    'DESTINATION-OF': 'RUN-66',
                                    'concept': 'DOOR',
                                    'from-sense': 'DOOR-N1',
                                    'is-in-subtree': 'OBJECT',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [43, [4]],
                                    'token': 'door'
                                },
                                'HUMAN-66': {
                                    'AGENT-OF': 'RUN-66',
                                    'concept': 'HUMAN',
                                    'from-sense': 'I-N1',
                                    'is-in-subtree': 'OBJECT',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [43, [0]],
                                    'token': 'I'
                                },
                                'RUN-66': {
                                    'AGENT': 'HUMAN-66',
                                    'DESTINATION': 'DOOR-66',
                                    'TIME': ['<', 'FIND-ANCHOR-TIME'],
                                    'concept': 'RUN',
                                    'from-sense': 'RUN-V1',
                                    'is-in-subtree': 'EVENT',
                                    'preference': 6.0,
                                    'sem-preference': 6,
                                    'sent-word-ind': [43, [1, 2]],
                                    'token': 'ran'
                                },
                                'baseline-semantic-score': 3,
                                'combined-score': 16.0,
                                'semantic-score': 6,
                                'syntactic-score': 14.0
                            },
                            'concept_counts': {
                                'DOOR': {
                                    'count': 66,
                                    'word-info': [[4, 'top']]
                                },
                                'HUMAN': {
                                    'count': 66,
                                    'word-info': [[0, 'top']]
                                },
                                'RUN': {
                                    'count': 66,
                                    'word-info': [[1, 'top']]
                                }
                            },
                            'words': {
                                0: ['I', 'I-N1', '$VAR0=0', 1],
                                1: ['RUN', 'RUN-V1', '$VAR0=1,$VAR1=0', 1],
                                2: ['TO', 'TO-PREP2', '$VAR0=2,$VAR1=1,$VAR2=4', 1],
                                4: ['DOOR', 'DOOR-N1', '$VAR0=4', 1],
                                5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                            }
                        }
                    ],
                    'sent-num': 43,
                    'sentence': 'I ran to the door.',
                    'timestamp': '2020-Mar-22 21:18:46'
                },



                {
                    'OriginalSentence': 'Biss has run a good campaign, but we prefer Coulson.',
                    'ambiguous-words': {},
                    'candidatesBeforePruning': 492,
                    'min-maxScores': [26.5, 42.0],
                    'results': [
                        {
                            'TMR': {
                                'ASPECT-67': {
                                    'PHASE': 'BEGIN-CONTINUE-END',
                                    'SCOPE': 'SUPERVISE-67',
                                    'concept': 'ASPECT',
                                    'from-sense': 'HAVE-AUX2',
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [1]],
                                    'token': 'has'
                                },
                                'HUMAN-67': {
                                    'AGENT-OF': 'SUPERVISE-67',
                                    'HAS-PERSONAL-NAME': 'BISS',
                                    'concept': 'HUMAN',
                                    'from-sense': 'PERSON-NAME',
                                    'is-in-subtree': 'OBJECT',
                                    'lex-source': 'NER',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [0]],
                                    'token': 'Biss'
                                },
                                'HUMAN-68': {
                                    'HAS-PERSONAL-NAME': 'COULSON',
                                    'SCOPE-OF': 'MODALITY-67',
                                    'concept': 'HUMAN',
                                    'from-sense': 'PERSON-NAME',
                                    'is-in-subtree': 'OBJECT',
                                    'lex-source': 'NER',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [10]],
                                    'token': 'Coulson'
                                },
                                'MODALITY-67': {
                                    'ATTRIBUTED-TO': 'SET-67',
                                    'DISCOURSE-RELATION-INVERSE':
                                    'SUPERVISE-67',
                                    'SCOPE': 'HUMAN-68',
                                    'TIME': ['FIND-ANCHOR-TIME'],
                                    'TYPE': 'EVALUATIVE',
                                    'VALUE': 1,
                                    'concept': 'MODALITY',
                                    'from-sense': 'PREFER-V2',
                                    'preference': 4.0,
                                    'sem-preference': 2,
                                    'sent-word-ind': [44, [9]],
                                    'token': 'prefer'
                                },
                                'MODALITY-68': {
                                    'SCOPE': 'POLITICAL-CAMPAIGN-67',
                                    'TYPE': 'EVALUATIVE',
                                    'VALUE': 0.7,
                                    'concept': 'MODALITY',
                                    'from-sense': 'GOOD-ADJ2',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [4]],
                                    'token': 'good'
                                },
                                'POLITICAL-CAMPAIGN-67': {
                                    'SCOPE-OF': 'MODALITY-68',
                                    'THEME-OF': 'SUPERVISE-67',
                                    'concept': 'POLITICAL-CAMPAIGN',
                                    'from-sense': 'CAMPAIGN-N2',
                                    'is-in-subtree': 'EVENT',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [5]],
                                    'token': 'campaign'
                                },
                                'SET-67': {
                                    'ATTRIBUTION': 'MODALITY-67',
                                    'CARDINALITY': ['>', 1],
                                    'MEMBER-TYPE': 'HUMAN',
                                    'concept': 'SET',
                                    'from-sense': 'WE-N1',
                                    'is-in-subtree': 'PROPERTY',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [44, [8]],
                                    'token': 'we'
                                },
                                'SUPERVISE-67': {
                                    'AGENT': 'HUMAN-67',
                                    'CONTRAST': 'MODALITY-67',
                                    'SCOPE-OF': 'ASPECT-67',
                                    'THEME': 'POLITICAL-CAMPAIGN-67',
                                    'TIME': ['FIND-ANCHOR-TIME'],
                                    'concept': 'SUPERVISE',
                                    'from-sense': 'HANDLE-V2',
                                    'is-in-subtree': 'EVENT',
                                    'preference': 16.0,
                                    'sem-preference': 4,
                                    'sent-word-ind': [44, [2, 1, 7]],
                                    'token': 'run'
                                },
                                'baseline-semantic-score': 3,
                                'combined-score': 42.0,
                                'semantic-score': 6,
                                'syntactic-score': 40.0},
                                'concept_counts': {
                                    'ASPECT': {
                                        'count': 67,
                                        'word-info': [[1, 'top']]
                                    },
                                'HUMAN': {
                                    'count': 68,
                                    'word-info': [[0, 'top'], [10, 'top']]
                                },
                                'MODALITY': {
                                    'count': 69,
                                    'word-info': [[9, 'top'], [4, 'top'], [7, 'top']]
                                },
                                'POLITICAL-CAMPAIGN': {
                                    'count': 67,
                                    'word-info': [[5, 'top']]
                                },
                                'SET': {
                                    'count': 67,
                                    'word-info': [[8, 'top']]
                                },
                                'SUPERVISE': {
                                    'count': 67,
                                    'word-info': [[2, 'top']]
                                }
                            },
                            'words': {
                                0: ['BISS', 'PERSON-NAME', '$VAR0=0', 1],
                                1: ['HAVE', 'HAVE-AUX2', '$VAR0=1,$VAR1=2', 1],
                                2: ['RUN', 'HANDLE-V2', '$VAR0=2,$VAR1=0,$VAR2=5', 1],
                                4: ['GOOD', 'GOOD-ADJ2', '$VAR0=4,$VAR1=5', 1],
                                5: ['CAMPAIGN', 'CAMPAIGN-N2', '$VAR0=5', 1],
                                6: [',', ',-PUNCT1', '$VAR0=6', 1],
                                7: ['BUT', 'BUT-CONJ1', '$VAR0=7,$VAR1=2,$VAR2=9,$VAR3=6', 1],
                                8: ['WE', 'WE-N1', '$VAR0=8', 1],
                                9: ['PREFER', 'PREFER-V2', '$VAR0=9,$VAR1=8,$VAR2=10', 1],
                                10: ['COULSON', 'PERSON-NAME', '$VAR0=10', 1],
                                11: ['.', '.-PUNCT1', '$VAR0=11', 1]
                            }
                        }
                    ],
                    'sent-num': 44,
                    'sentence': 'Biss has run a good campaign, but we prefer Coulson.',
                    'timestamp': '2020-Mar-22 21:18:47'
                },



                {
                    'OriginalSentence': 'We will rise up.',
                    'ambiguous-words': {},
                    'candidatesBeforePruning': 15,
                    'min-maxScores': [-4.0, 14.0],
                    'results': [
                        {
                            'TMR': {
                                'REBEL-70': {
                                    'AGENT': 'SET-70',
                                    'TIME': ['>', 'FIND-ANCHOR-TIME'],
                                    'concept': 'REBEL',
                                    'from-sense': 'RISE-V7',
                                    'is-in-subtree': 'EVENT',
                                    'preference': 8.0,
                                    'sem-preference': 2,
                                    'sent-word-ind': [45, [2]],
                                    'token': 'rise'
                                },
                                'SET-70': {
                                    'AGENT-OF': 'REBEL-70',
                                    'CARDINALITY': ['>', 1],
                                    'MEMBER-TYPE': 'HUMAN',
                                    'concept': 'SET',
                                    'from-sense': 'WE-N1',
                                    'is-in-subtree': 'PROPERTY',
                                    'preference': 4.0,
                                    'sem-preference': 0,
                                    'sent-word-ind': [45, [0]],
                                    'token': 'We'
                                },
                                'baseline-semantic-score': 1,
                                'combined-score': 14.0,
                                'semantic-score': 2,
                                'syntactic-score': 12.0},
                                'concept_counts': {
                                    'REBEL': {
                                        'count': 70,
                                        'word-info': [[2, 'top']]
                                    },
                                    'SET': {
                                        'count': 72,
                                        'word-info': [[0, 'top'], [1001, 'top'], [1002, 'top']]
                                    }
                                },
                                'words': {
                                    0: ['WE', 'WE-N1', '$VAR0=0', 1],
                                    1: ['WILL', 'WILL-AUX1', '$VAR0=1,$VAR1=2', 1],
                                    2: ['RISE', 'RISE-V7', '$VAR0=2,$VAR1=0,$VAR2=3,$VAR3=None,$VAR4=None', 1],
                                    4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                                }
                            }
                        ],
                        'sent-num': 45,
                        'sentence': 'We will rise up.',
                        'timestamp': '2020-Mar-22 21:18:47'
                    },


        {
            'OriginalSentence': 'A dinner bell rang.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 1,
            'min-maxScores': [14.0, 14.0],
            'results': [
                {
                    'TMR': {
                        'BELL-73': {
                            'INSTRUMENT-OF': 'RING-EVENT-73',
                            'RANGE-OF': 'RELATION-73',
                            'concept': 'BELL',
                            'from-sense': 'BELL-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [46, [2]],
                            'token': 'bell'
                        },
                        'DINNER-73': {
                            'DOMAIN-OF': 'RELATION-73',
                            'concept': 'DINNER',
                            'from-sense': 'DINNER-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [46, [1]],
                            'token': 'dinner'
                        },
                        'RELATION-73': {
                            'DOMAIN': 'DINNER-73',
                            'RANGE': 'BELL-73',
                            'concept': 'RELATION',
                            'is-in-subtree': 'PROPERTY',
                            'sem-preference': 0
                        },
                        'RING-EVENT-73': {
                            'INSTRUMENT': 'BELL-73',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'RING-EVENT',
                            'from-sense': 'RING-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [46, [3]],
                            'token': 'rang'
                        },
                        'baseline-semantic-score': 1,
                        'combined-score': 14.0,
                        'semantic-score': 2,
                        'syntactic-score': 12.0
                    },
                    'concept_counts': {
                        'BELL': {
                            'count': 73,
                            'word-info': [[2, 'top']]
                        },
                        'DINNER': {
                            'count': 73,
                            'word-info': [[1, 'top']]
                        },
                        'RING-EVENT': {
                            'count': 73,
                            'word-info': [[3, 'top']]
                        }
                    },
                    'words': {
                        1: ['DINNER', 'DINNER-N1', '$VAR0=1', 1],
                        2: ['BELL', 'BELL-N1', '$VAR0=2', 1],
                        3: ['RING', 'RING-V2', '$VAR0=3,$VAR1=2', 1],
                        4: ['.', '.-PUNCT1', '$VAR0=4', 1]
                    }
                }
            ],
            'sent-num': 46,
            'sentence': 'A dinner bell rang.',
            'timestamp': '2020-Mar-22 21:18:47'
        },


        {
            'OriginalSentence': 'We rented a station wagon.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 1,
            'min-maxScores': [14.5, 14.5],
            'results': [
                {
                    'TMR': {
                        'RENT-OUT-74': {
                            'BENEFICIARY': 'SET-74',
                            'THEME': 'STATION-WAGON-74',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'RENT-OUT',
                            'from-sense': 'RENT-V3',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 5,
                            'sent-word-ind': [47, [1]],
                            'token': 'rented'
                        },
                        'SET-74': {
                            'BENEFICIARY-OF': 'RENT-OUT-74',
                            'CARDINALITY': ['>', 1],
                            'MEMBER-TYPE': 'HUMAN',
                            'concept': 'SET',
                            'from-sense': 'WE-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [47, [0]],
                            'token': 'We'
                        },
                        'STATION-WAGON-74': {
                            'THEME-OF': 'RENT-OUT-74',
                            'concept': 'STATION-WAGON',
                            'from-sense':
                            'STATION_WAGON-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [47,[3]],
                            'token': 'STATION_WAGON'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 14.5,
                        'semantic-score': 5,
                        'syntactic-score': 12.0
                    },
                    'concept_counts': {
                        'RENT-OUT': {
                            'count': 74,
                            'word-info': [[1, 'top']]
                        },
                        'SET': {
                            'count': 74,
                            'word-info': [[0, 'top']]
                        },
                        'STATION-WAGON': {
                            'count': 74,
                            'word-info': [[3, 'top']]
                        }
                    },
                    'words': {
                        0: ['WE', 'WE-N1', '$VAR0=0', 1],
                        1: ['RENT', 'RENT-V3', '$VAR0=1,$VAR1=0,$VAR2=3,$VAR3=None,$VAR4=None', 1],
                        3: ['STATION_WAGON', 'STATION_WAGON-N1', '$VAR0=3', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 47,
            'sentence': 'We rented a STATION_WAGON.',
            'timestamp': '2020-Mar-22 21:18:47'
        },



        {
            'OriginalSentence': 'The NCAA releases the information.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 6,
            'min-maxScores': [7.0, 13.0],
            'results': [
                {
                    'TMR': {
                        'ENTITY-75': {
                            'AGENT-OF': 'INFORM-75',
                            'HAS-NAME': 'NCAA',
                            'concept': 'ENTITY',
                            'from-sense': 'OTHER-NAME',
                            'lex-source': 'NER',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [48, [1]],
                            'token': 'NCAA'
                        },
                        'INFORM-75': {
                            'AGENT': 'ENTITY-75',
                            'THEME': 'INFORMATION-75',
                            'TIME': ['FIND-ANCHOR-TIME'],
                            'concept': 'INFORM',
                            'from-sense': 'RELEASE-V4',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [48, [2]],
                            'token': 'releases'
                        },
                        'INFORMATION-75': {
                            'THEME-OF': 'INFORM-75',
                            'concept': 'INFORMATION',
                            'from-sense': 'INFORMATION-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [48, [4]],
                            'token': 'information'
                        },
                        'baseline-semantic-score': 2,
                        'combined-score': 13.0,
                        'semantic-score': 2,
                        'syntactic-score': 12.0
                    },
                    'concept_counts': {
                        'ENTITY': {
                            'count': 75,
                            'word-info': [[1, 'top']]
                        },
                        'INFORM': {
                            'count': 75,
                            'word-info': [[2, 'top']]
                        },
                        'INFORMATION': {
                            'count': 75,
                            'word-info': [[4, 'top']]
                        }
                    },
                    'words': {
                        1: ['NCAA', 'OTHER-NAME', '$VAR0=1', 1],
                        2: ['RELEASE', 'RELEASE-V4', '$VAR0=2,$VAR1=1,$VAR2=4', 1],
                        4: ['INFORMATION', 'INFORMATION-N1', '$VAR0=4', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 48,
            'sentence': 'The NCAA releases the information.',
            'timestamp': '2020-Mar-22 21:18:47'
        },


        {
            'OriginalSentence': 'USAID refused interviews with staff in Badakhshan.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 476,
            'min-maxScores': [19.9, 29.5],
            'results': [
                {
                    'TMR': {
                        'ACCEPT-76': {
                            'AGENT': 'ENTITY-76',
                            'SCOPE-OF': 'MODALITY-76',
                            'THEME': 'INTERVIEW-76',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'concept': 'ACCEPT',
                            'from-sense': 'REFUSE-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 4.0,
                            'sem-preference': 2,
                            'sent-word-ind': [49, [1]],
                            'token': 'refused'
                        },
                        'ENTITY-76': {
                            'AGENT-OF': 'ACCEPT-76',
                            'HAS-NAME': 'USAID',
                            'concept': 'ENTITY',
                            'from-sense': 'OTHER-NAME',
                            'lex-source': 'NER',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [49, [0]],
                            'token': 'USAID'
                        },
                        'INTERVIEW-76': {
                            'AGENT': 'SET-76',
                            'CARDINALITY': ['>', 1],
                            'THEME-OF': 'ACCEPT-76',
                            'concept': 'INTERVIEW',
                            'from-sense': 'INTERVIEW-N1',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 2,
                            'sent-word-ind': [49, [2, 3]],
                            'token': 'interviews'
                        },
                        'MODALITY-76': {
                            'SCOPE': 'ACCEPT-76',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'TYPE': 'EPISTEMIC',
                            'VALUE': 0,
                            'concept': 'MODALITY',
                            'from-sense': 'REFUSE-V2',
                            'sem-preference': 0,
                            'sent-word-ind': [49, [1]],
                            'token': 'refused'
                        },
                        'PROVINCE-76': {
                            'HAS-NAME': 'BADAKHSHAN',
                            'LOCATION-OF': 'SET-76',
                            'concept': 'PROVINCE',
                            'from-sense': 'OTHER-NAME',
                            'is-in-subtree': 'OBJECT',
                            'lex-source': 'onomasticon',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [49, [6]],
                            'token': 'Badakhshan'
                        },
                        'SET-76': {
                            'AGENT-OF': 'INTERVIEW-76',
                            'CARDINALITY': ['>', 1],
                            'LOCATION': 'PROVINCE-76',
                            'MEMBER-TYPE': 'WORK-ROLE',
                            'concept': 'SET',
                            'from-sense': 'STAFF-N1',
                            'is-in-subtree': 'PROPERTY',
                            'preference': 8.0,
                            'sem-preference': 2,
                            'sent-word-ind': [49, [4, 5]],
                            'token': 'staff'
                        },
                        'baseline-semantic-score': 4,
                        'combined-score': 29.5,
                        'semantic-score': 6,
                        'syntactic-score': 28.0},
                        'concept_counts': {
                            'ACCEPT': {
                                'count': 76,
                                'word-info': [[1, 'top']]
                            },
                            'ENTITY': {
                                'count': 76,
                                'word-info': [[0, 'top']]
                            },
                            'INTERVIEW': {
                                'count': 76,
                                'word-info': [[2, 'top']]
                            },
                            'MODALITY': {
                                'count': 76,
                                'word-info': [[1, 'top']]
                            },
                            'PROVINCE': {
                                'count': 76,
                                'word-info': [[6, 'top']]
                            },
                        'SET': {
                            'count': 76,
                            'word-info': [[4, 'top']]
                        }
                    },
                    'words': {
                        0: ['USAID', 'OTHER-NAME', '$VAR0=0', 1],
                        1: ['REFUSE', 'REFUSE-V2', '$VAR0=1,$VAR1=0,$VAR2=2', 1],
                        2: ['INTERVIEW', 'INTERVIEW-N1', '$VAR0=2,$VAR1=None,$VAR2=None,$VAR3=None,$VAR4=None', 1],
                        3: ['WITH', 'WITH-PREP1', '$VAR0=3,$VAR1=2,$VAR2=4', 1],
                        4: ['STAFF', 'STAFF-N1', '$VAR0=4', 1],
                        5: ['IN', 'IN-PREP1', '$VAR0=5,$VAR1=4,$VAR2=6', 1],
                        6: ['BADAKHSHAN', 'OTHER-NAME', '$VAR0=6', 1],
                        7: ['.', '.-PUNCT1', '$VAR0=7', 1]
                    }
                }
            ],
            'sent-num': 49,
            'sentence': 'USAID refused interviews with staff in Badakhshan.',
            'timestamp': '2020-Mar-22 21:18:48'
        },


        {
            'OriginalSentence': 'She raced to the church.',
            'ambiguous-words': {},
            'candidatesBeforePruning': 3,
            'min-maxScores': [4.0, 18.3],
            'results': [
                {
                    'TMR': {
                        'CHURCH-BUILDING-77': {
                            'DESTINATION-OF': 'MOTION-EVENT-77',
                            'concept': 'CHURCH-BUILDING',
                            'from-sense': 'CHURCH-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [50, [4]],
                            'token': 'church'
                        },
                        'HUMAN-77': {
                            'AGENT-OF': 'MOTION-EVENT-77',
                            'GENDER': 'FEMALE',
                            'concept': 'HUMAN',
                            'from-sense': 'SHE-N1',
                            'is-in-subtree': 'OBJECT',
                            'preference': 4.0,
                            'sem-preference': 0,
                            'sent-word-ind': [50, [0]],
                            'token': 'She'
                        },
                        'MOTION-EVENT-77': {
                            'AGENT': 'HUMAN-77',
                            'DESTINATION': 'CHURCH-BUILDING-77',
                            'TIME': ['<', 'FIND-ANCHOR-TIME'],
                            'VELOCITY': ['>', 0.8],
                            'concept': 'MOTION-EVENT',
                            'from-sense': 'RACE-V2',
                            'is-in-subtree': 'EVENT',
                            'preference': 8.0,
                            'sem-preference': 7,
                            'sent-word-ind': [50, [1,
                            2]],
                            'token': 'raced'
                        },
                        'baseline-semantic-score': 3,
                        'combined-score': 18.33,
                        'semantic-score': 7,
                        'syntactic-score': 16.0
                    },
                    'concept_counts': {
                        'CHURCH-BUILDING': {
                            'count': 77,
                            'word-info': [[4, 'top']]
                        },
                        'HUMAN': {
                            'count': 77,
                            'word-info': [[0, 'top']]
                        },
                        'MOTION-EVENT': {
                            'count': 77,
                            'word-info': [[1, 'top']]
                        }
                    },
                    'words': {
                        0: ['SHE', 'SHE-N1', '$VAR0=0', 1],
                        1: ['RACE', 'RACE-V2', '$VAR0=1,$VAR1=0', 1],
                        2: ['TO', 'TO-PREP2', '$VAR0=2,$VAR1=1,$VAR2=4', 1],
                        4: ['CHURCH', 'CHURCH-N1', '$VAR0=4', 1],
                        5: ['.', '.-PUNCT1', '$VAR0=5', 1]
                    }
                }
            ],
            'sent-num': 50,
            'sentence': 'She raced to the church.',
            'timestamp': '2020-Mar-22 21:18:48'
        }
]
