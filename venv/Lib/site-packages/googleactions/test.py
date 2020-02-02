from marshmallow import pprint
from googleactions.models import *
from googleactions.builders import *

request = {
    "user": {
        "userId": "wCBxFjVLK8I+nxIXfFOHEf/iAvvaTFuzUdBw6Gv5K3Q="
    },
    "userStorage": "{\"key1\": \"value1\", \"key2\": \"value2\"}",
    "conversation": {
        "conversationId": "1494709404186",
        "type": "NEW"
    },
    "inputs": [
        {
            "intent": "actions.intent.MAIN",
            "rawInputs": [
                {
                    "inputType": "KEYBOARD",
                    "query": "talk to my test app"
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "availableSurfaces": [{
        "capabilities": [
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            },
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.MEDIA_RESPONSE_AUDIO"
            },
            {
                "name": "actions.capability.WEB_BROWSER"
            }
        ]
    }]
}

response = {
    "conversationToken": "token",
    "expectUserResponse": True,
    "expectedInputs": [
        {
            "inputPrompt": {
                "richInitialPrompt": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": ("Howdy! I can tell you fun facts about almost any number, like 42. "
                                                 "What do you have in mind?"),
                                "displayText": ("Howdy! I can tell you fun facts about almost any number. "
                                                "What do you have in mind?")
                            }
                        }
                    ],
                    "suggestions": []
                }
            },
            "possibleIntents": [
                {
                    "intent": "actions.intent.TEXT"
                }
            ]
        }
    ]
}

request_option = {
    "user": {
        "userId": "123456abcde",
        "locale": "en-US"
    },
    "conversation": {
        "conversationId": "123456",
        "type": "ACTIVE",
        "conversationToken": ""
    },
    "inputs": [
        {
            "intent": "actions.intent.OPTION",
            "rawInputs": [
                {
                    "inputType": "VOICE",
                    "query": "42 recipes with 42 ingredients"
                }
            ],
            "arguments": [
                {
                    "name": "OPTION",
                    "textValue": "RECIPES"
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "isInSandbox": True,
    "availableSurfaces": [
        {
            "capabilities": [
                {
                    "name": "actions.capability.AUDIO_OUTPUT"
                },
                {
                    "name": "actions.capability.SCREEN_OUTPUT"
                }
            ]
        }
    ]
}

perm_granted = {
    "user": {
        "userId": "user123",
        "profile": {
            "displayName": "Jane Smith",
            "givenName": "Jane",
            "familyName": "Smith"
        }
    },
    "conversation": {
        "conversationId": "1494884577894",
        "type": "ACTIVE",
        "conversationToken": "{\"state\":null,\"data\":{}}"
    },
    "inputs": [
        {
            "intent": "actions.intent.PERMISSION",
            "rawInputs": [
                {
                    "inputType": "KEYBOARD",
                    "query": "yes"
                }
            ],
            "arguments": [
                {
                    "name": "PERMISSION",
                    "rawText": "yes",
                    "textValue": "true"
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "device": {
        "location": {
            "coordinates": {
                "latitude": 37.422366,
                "longitude": -122.084406
            },
            "formattedAddress": "1600 Amphitheatre Parkway, Mountain View, CA 94043, United States",
            "zipCode": "94043",
            "city": "Mountain View"
        },
        "locale": "en-US"
    },
    "isInSandbox": False
}

req_date_time = {
    "user": {
        "userId": "user123"
    },
    "conversation": {
        "conversationId": "1494884466160",
        "type": "ACTIVE",
        "conversationToken": "{\"state\":null,\"data\":{}}"
    },
    "inputs": [
        {
            "intent": "actions.intent.DATETIME",
            "rawInputs": [
                {
                    "inputType": "VOICE",
                    "query": "tuesday at 9"
                }
            ],
            "arguments": [
                {
                    "name": "DATETIME",
                    "datetimeValue": {
                        "date": {
                            "year": 2017,
                            "month": 5,
                            "day": 16
                        },
                        "time": {
                            "hours": 9
                        }
                    }
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "device": {
        "locale": "en-US"
    },
    "isInSandbox": False
}

req_sign_in = {
    "isInSandbox'": False,
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "inputs": [
        {
            "rawInputs": [
                {
                    "query": "i think so",
                    "inputType": "VOICE"
                }
            ],
            "arguments": [
                {
                    "name": "SIGN_IN",
                    'extension': {
                        "@type": "type.googleapis.com/google.actions.v2.SignInValue",
                        "status": "OK"
                    }
                }
            ],
            "intent": "actions.intent.SIGN_IN"
        }
    ],
    "user": {
        "userId": "user123",
        "accessToken": "12345"
    },
    "device": {
        "locale": "en-US"
    },
    "conversation": {
        "conversationId": "1494606917128",
        "type": "ACTIVE",
        "conversationToken": "[\"_actions_on_google_\"]"
    }
}

req_conf = {
    "user": {
        "userId": "user123"
    },
    "conversation": {
        "conversationId": "1494884269122",
        "type": "ACTIVE",
        "conversationToken": "{\"state\":null,\"data\":{}}"
    },
    "inputs": [
        {
            "intent": "actions.intent.CONFIRMATION",
            "rawInputs": [
                {
                    "inputType": "VOICE",
                    "query": "yes"
                }
            ],
            "arguments": [
                {
                    "name": "CONFIRMATION",
                    "boolValue": True
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "device": {
        "locale": "en-US"
    },
    "isInSandbox": False
}

req_link = {
    "user": {
        "userId": "user123"
    },
    "conversation": {
        "conversationId": "1494884269122",
        "type": "ACTIVE",
        "conversationToken": "{\"state\":null,\"data\":{}}"
    },
    "inputs": [
        {
            "intent": "actions.intent.LINK",
            "arguments": [
                {
                    "name": "LINK",
                    "status": {
                        "code": 9
                    }
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    },
    "device": {
        "locale": "en-US"
    },
    "isInSandbox": False
}

req_surf = {
    "user": {
        "userId": "1234",
        "locale": "en-US"
    },
    "conversation": {
        "conversationId": "1234",
        "type": "ACTIVE",
        "conversationToken": ""
    },
    "inputs": [
        {
            "intent": "actions.intent.NEW_SURFACE",
            "rawInputs": [
                {
                    "inputType": "VOICE",
                    "query": "[request notification]"
                }
            ],
            "arguments": [
                {
                    "name": "NEW_SURFACE",
                    "extension": {
                        "@type": "type.googleapis.com/google.actions.v2.NewSurfaceValue",
                        "status": "OK"
                    }
                }
            ]
        }
    ],
    "surface": {
        "capabilities": [
            {
                "name": "actions.capability.AUDIO_OUTPUT"
            },
            {
                "name": "actions.capability.SCREEN_OUTPUT"
            }
        ]
    }
}


def test_app_request():
    app_request = AppRequest.deserialize(request)
    result = AppRequest.serialize(app_request)
    pprint(vars(app_request))
    pprint(result, indent=2)


def test_app_response():
    app_response = AppResponse.deserialize(response)
    result = AppResponse.serialize(app_response)
    pprint(vars(app_response))
    pprint(result, indent=2)


def test_conversation():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Hello'))
            .build(as_json=True))


def test_ssml():
    ssml = (SsmlBuilder()
            .start_p()
            .start_s()
            .emphasis('If you build it, they will come', level=EmphasisLevel.STRONG)
            .end_s()
            .end_p()
            .do_break(1)
            .text('Its over')
            .say_as('9000', interpret_as=InterpretAs.CARDINAL)
            .prosody('What the', rate=ProsodyRate.SLOW)
            .say_as('fuck', interpret_as=InterpretAs.EXPLETIVE)
            .do_break(1)
            .sub('brb', alias='Be right back')
            .do_break(1)
            .prosody('High!', rate=ProsodyRate.DEFAULT, pitch=ProsodyPitch.HIGH)
            .start_par()
            .start_media(id='gun')
            .audio(src='https://actions.google.com/sounds/v1/weapons/automatic_gun.ogg',
                           clip_begin='1s',
                           clip_end='2s')
            .end_media()
            .start_media(begin='gun.end+1.0s')
            .audio(src='https://actions.google.com/sounds/v1/animals/dog_barking.ogg',
                           clip_begin='8s',
                           clip_end='10s',
                           desc='desc',
                           alt='alt')
            .end_media()
            .end_par()
            .build())
    print(ssml)

    urmom = (SsmlBuilder()
             .start_par()
             .start_media('a')
             .text(SsmlBuilder().text('Your mothers').build())
             .end_media()
             .start_media('b', begin='a.end-0.3s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW, pitch=ProsodyPitch.X_HIGH)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('c', begin='b.end+0.2s')
             .text(SsmlBuilder().text('is so nasty I had to').build())
             .end_media()
             .start_media('d', begin='c.end-0.3s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('e', begin='d.end+0.2s')
             .text(SsmlBuilder().text('clean my').build())
             .end_media()
             .start_media('f', begin='e.end-0.3s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('g', begin='f.end+0.2s')
             .text(SsmlBuilder().text('with a').build())
             .end_media()
             .start_media('h', begin='g.end-0.3s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('i', begin='h.end+0.2s')
             .text(SsmlBuilder().text('jesus').build())
             .end_media()
             .start_media(id='j', begin='i.end-0.3s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('k', begin='j.end-0.2s')
             .text(SsmlBuilder()
                   .start_prosody(rate=ProsodyRate.X_SLOW)
                   .say_as('~', interpret_as=InterpretAs.EXPLETIVE)
                   .end_prosody()
                   .build())
             .end_media()
             .start_media('l', begin='k.end+0.2s')
             .text(SsmlBuilder().text('goodbye').build())
             .end_media()
             .start_media('m', begin='l.end-0.2s')
             .audio(src='https://actions.google.com/sounds/v1/doors/door_slams_fast_four_times.ogg',
                    clip_begin='1s',
                    clip_end='3s')
             .end_media()
             .end_par()
             .build())

    print(urmom)


def test_ssml_conv():
    conv = (ConversationBuilder()
            .do(SimpleResponse(ssml=SsmlBuilder()
                               .audio(src='https://actions.google.com/sounds/v1/animals/dog_barking.ogg')
                               .build()))
            .build(as_json=True))


def test_basic_card():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(basic_card=BasicCard(title='Title',
                                     subtitle='Subtitle',
                                     text='*emphasis* _italics_ **strong** __bold__ ***bold itallic***'
                                          ' ___strong emphasis___ \nbreaks',
                                     image=Image(url='https://goo.gl/images/S4mm27', alt='Cowgirl'),
                                     button=Button(url='https://google.com', title='Google')))
            .build(as_json=True))


def test_list():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(the_list=List(title='List Title',
                              items=[
                              ListItem(title='Title of First List Item',
                                       description='This is a description of a list item',
                                       image=Image(url='url',
                                                   alt='Image alternate text'),
                                       option_info=OptionInfo(key='1', synonyms=['1', '2', '3'])),
                              ListItem(title='Title of Second List Item',
                                       description='This is a description of a list item',
                                       image=Image(url='url',
                                                   alt='Image alternate text'),
                                       option_info=OptionInfo(key='2', synonyms=['1', '2', '3'])),
                              ListItem(title='Title of Third List Item',
                                       description='This is a description of a list item',
                                       image=Image(url='url',
                                                   alt='Image alternate text'),
                                       option_info=OptionInfo(key='3', synonyms=['1', '2', '3']))
                          ]))
            .build(as_json=True))
    write(conv)


def test_gso():
    app_request = AppRequest.deserialize(request_option)
    if app_request.get_input(Intent.OPTION):
        print(app_request.get_selected_option())


def test_carousel():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(carousel=Carousel(items=[
                              CarouselItem(title='Title of First Carousel Item',
                                                 description='This is a description of a carousel item',
                                                 image=Image(url='url',
                                                             alt='Image alternate text'),
                                                 option_info=OptionInfo(key='1', synonyms=['1', '2', '3'])),
                              CarouselItem(title='Title of Second Carousel Item',
                                                 description='This is a description of a carousel item',
                                                 image=Image(url='url',
                                                             alt='Image alternate text'),
                                                 option_info=OptionInfo(key='2', synonyms=['1', '2', '3'])),
                              CarouselItem(title='Title of Third Carousel Item',
                                                 description='This is a description of a carousel item',
                                                 image=Image(url='url',
                                                             alt='Image alternate text'),
                                                 option_info=OptionInfo(key='3', synonyms=['1', '2', '3']))
            ]))
            .build(as_json=True))
    write(conv)


def test_carousel_browse():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(carousel_browse=CarouselBrowse(items=[
                            CarouselBrowseItem(title='Title 1',
                                               description='Description',
                                               footer='Footer',
                                               image=Image(url='url', alt='alt'),
                                               url='url'),
                            CarouselBrowseItem(title='Title 2',
                                               description='Description',
                                               footer='Footer',
                                               image=Image(url='url', alt='alt'),
                                               url='url'),
                            CarouselBrowseItem(title='Title 3',
                                               description='Description',
                                               footer='Footer',
                                               image=Image(url='url', alt='alt'),
                                               url='url'),
            ]))
            .build(as_json=True))
    write(conv)


def test_suggestion():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(suggestions=Suggestion('Suggestion 1'))
            .build(as_json=True))
    write(conv)


def test_suggestions():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(suggestions=[Suggestion('Suggestion 1'), Suggestion('Suggestion 2'), Suggestion('Suggestion 3')])
            .build(as_json=True))
    write(conv)


def test_suggestion_short():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(suggestions='Suggestion 1')
            .build(as_json=True))
    write(conv)


def test_suggestions_short():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(suggestions=['Suggestion 1', 'Suggestion 2', 'Suggestion 3'])
            .build(as_json=True))
    write(conv)


def test_link_out_suggestion():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(link_out_suggestion=LinkOutSuggestion(name='Name', url='Url'))
            .build(as_json=True))
    write(conv)


def test_media():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(media_audio=MediaObject(name="Name",
                                        url='https://google.com/file.mp3',
                                        description='A music file',
                                        icon=Image(url='url', alt='alt')))
            .build(as_json=True))
    write(conv)


def test_table():
    conv = (ConversationBuilder()
            .do(SimpleResponse(speech='Text'))
            .do(table=TableCardBuilder()
                .row(['11', '12', '13'], True)
                .row(['21', '22', '23'], True)
                .row(['31', '32', '33'], False)
                .image(Image(url='url', alt='alt'))
                .button(Button(title='title', url='url'))
                .headers(['H1', 'H2', 'H3'])
                .build())
            .build(as_json=True))
    write(conv)


def test_permission():
    conv = (ConversationBuilder()
            .permission(permissions=[PermissionType.NAME, PermissionType.LOCATION], permission_context='To do things')
            .build(as_json=True))

    app_request = AppRequest.deserialize(perm_granted)
    if app_request.is_permission_granted():
        print(app_request.get_user())
        print(app_request.get_device())
    write(conv)


def test_date_time():
    conv = (ConversationBuilder()
            .helper_datetime(date_time_text='Pick a date and time',
                             date_text='Pick a date',
                             time_text='Pick a time')
            .build(as_json=True))
    write(conv)
    app_request = AppRequest.deserialize(req_date_time)
    date_time = app_request.get_helper_date_time()
    print(date_time.date.day)


def test_sign_in():
    conv = (ConversationBuilder()
            .helper_sign_in()
            .build(as_json=True))
    write(conv)
    app_request = AppRequest.deserialize(req_sign_in)
    if app_request.is_helper_signed_in():
        print(app_request.get_helper_sign_in_access_token())


def test_place():
    conv = (ConversationBuilder()
            .helper_place(place_prompt='Pick a place',
                          permission_context='To find where you are')
            .build(as_json=True))
    write(conv)


def test_conf():
    conv = (ConversationBuilder()
            .helper_confirmation(question='Will you marry me?')
            .build(as_json=True))
    app_request = AppRequest.deserialize(req_conf)
    print(app_request.get_helper_confirmation())
    write(conv)


def test_android_link():
    conv = (ConversationBuilder()
            .helper_android_link(url='https://www.service.com', package='com.service.consumer', reason='Because')
            .build(as_json=True))
    write(conv)
    app_request = AppRequest.deserialize(req_link)
    print(app_request.get_helper_link_status())


def test_capability():
    app_request = AppRequest.deserialize(request)
    print(app_request.has(Capability.AUDIO_OUTPUT))
    print(app_request.has(Capability.MEDIA_RESPONSE_AUDIO))
    print(app_request.has(Capability.SCREEN_OUTPUT))
    print(app_request.has(Capability.WEB_BROWSER))


def test_new_surface():
    app_request = AppRequest.deserialize(request)
    capabilities = [Capability.SCREEN_OUTPUT, Capability.AUDIO_OUTPUT]
    if app_request.has_surface(capabilities=capabilities):
        print('Can switch surfaces')
        write(ConversationBuilder()
              .helper_new_surface(ns_context='To do this',
                                  ns_notification_title='Images',
                                  capabilities=capabilities)
              .build(as_json=True))
    app_request_surf = AppRequest.deserialize(req_surf)
    print(app_request_surf.get_helper_new_surface())


def test_storage():
    write(ConversationBuilder().storage({'key1': 'value1', 'key2': 'value2'}).reset_storage().build(as_json=True))
    app_request = AppRequest.deserialize(request)
    if app_request.has_storage():
        print(app_request.get_storage())


def test_end():
    write(ConversationBuilder().do(simple=SimpleResponse(speech='Bye!')).end().build(as_json=True))


def write(obj):
    file = open('out.txt', 'w')
    file.write(obj)
    file.close()


if __name__ == "__main__":
    for i in range(0, 200):
        print('{}: {}'.format(i, chr(i)))
    # test_end()
    # test_storage()
    # test_new_surface()
    # test_capability()
    # test_android_link()
    # test_conf()
    # test_place()
    # test_sign_in()
    # test_date_time()
    # test_permission()
    # test_table()
    # test_media()
    # test_link_out_suggestion()
    # test_suggestions_short()
    # test_suggestion_short()
    # test_suggestions()
    # test_suggestion()
    # test_carousel_browse()
    # test_carousel()
    # test_gso()
    # test_list()
    # test_basic_card()
    # est_ssml_conv()
    # test_ssml()
    # test_conversation()
    # test_app_request()
    # test_app_response()
