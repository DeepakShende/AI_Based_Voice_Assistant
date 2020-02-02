import json
from googleactions.utils import flatten


class Intent(object):
    MAIN = 'actions.intent.MAIN'
    TEXT = 'actions.intent.TEXT'
    CANCEL = 'actions.intent.CANCEL'
    CONFIGURE_UPDATES = 'actions.intent.CONFIGURE_UPDATES'
    CONFIRMATION = 'actions.intent.CONFIRMATION'
    DATETIME = 'actions.intent.DATETIME'
    DELIVERY_ADDRESS = 'actions.intent.DELIVERY_ADDRESS'
    NEW_SURFACE = 'actions.intent.NEW_SURFACE'
    NO_INPUT = 'actions.intent.NO_INPUT'
    OPTION = 'actions.intent.OPTION'
    PERMISSION = 'actions.intent.PERMISSION'
    SIGN_IN = 'actions.intent.SIGN_IN'
    TRANSACTION_REQUIREMENTS_CHECK = 'actions.intent.TRANSACTION_REQUIREMENTS_CHECK'
    TRANSACTION_DECISION = 'actions.intent.TRANSACTION_DECISION'
    REGISTER_UPDATE = 'actions.intent.REGISTER_UPDATE'
    PLACE = 'actions.intent.PLACE'
    LINK = 'actions.intent.LINK'
    FALLBACK = 'input.unknown'


class PermissionType(object):
    NAME = 'NAME'
    LOCATION = 'DEVICE_PRECISE_LOCATION'
    UNSPECIFIED_PERMISSION = 'UNSPECIFIED_PERMISSION'
    DEVICE_COARSE_LOCATION = 'DEVICE_COARSE_LOCATION'
    UPDATE = 'UPDATE'


class Capability(object):
    SCREEN_OUTPUT = 'actions.capability.SCREEN_OUTPUT'
    AUDIO_OUTPUT = 'actions.capability.AUDIO_OUTPUT'
    MEDIA_RESPONSE_AUDIO = 'actions.capability.MEDIA_RESPONSE_AUDIO'
    WEB_BROWSER = 'actions.capability.WEB_BROWSER'


class ConversationType(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/ConversationType"""
    TYPE_UNSPECIFIED = 'TYPE_UNSPECIFIED'
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'


class InputType(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/InputType"""
    UNSPECIFIED_INPUT_TYPE = 'UNSPECIFIED_INPUT_TYPE'
    TOUCH = 'TOUCH'
    VOICE = 'VOICE'
    KEYBOARD = 'KEYBOARD'


class UrlTypeHint(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/UrlTypeHint"""
    URL_TYPE_HINT_UNSPECIFIED = 'URL_TYPE_HINT_UNSPECIFIED'
    AMP_CONTENT = 'AMP_CONTENT'


class ImageDisplayOptions(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/ImageDisplayOptions"""
    DEFAULT = 'DEFAULT'
    WHITE = 'WHITE'
    CROPPED = 'CROPPED'


class ActionType(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/ActionType"""
    UNKNOWN = 'UNKNOWN'
    VIEW_DETAILS = 'VIEW_DETAILS'
    MODIFY = 'MODIFY'
    CANCEL = 'CANCEL'
    RETURN = 'RETURN'
    EXCHANGE = 'EXCHANGE'
    EMAIL = 'EMAIL'
    CALL = 'CALL'
    REORDER = 'REORDER'
    REVIEW = 'REVIEW'
    CUSTOMER_SERVICE = 'CUSTOMER_SERVICE'
    FIX_ISSUE = 'FIX_ISSUE'


class MediaType(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/MediaType"""
    MEDIA_TYPE_UNSPECIFIED = 'MEDIA_TYPE_UNSPECIFIED'
    AUDIO = 'AUDIO'


class HorizontalAlignment(object):
    """https://developers.google.com/actions/reference/rest/Shared.Types/HorizontalAlignment"""
    LEADING = 'LEADING'
    CENTER = 'CENTER'
    TRAILING = 'TRAILING'


class AtType(object):
    OPTION_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.OptionValueSpec'
    PERMISSION_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.PermissionValueSpec'
    SIGN_IN_VALUE = 'type.googleapis.com/google.actions.v2.SignInValue'
    PLACE_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.PlaceValueSpec'
    PLACE_DIALOG_SPEC = 'type.googleapis.com/google.actions.v2.PlaceValueSpec.PlaceDialogSpec'
    CONFIRMATION_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.ConfirmationValueSpec'
    LINK_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.LinkValueSpec'
    NEW_SURFACE_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.NewSurfaceValueSpec'
    DATE_TIME_VALUE_SPEC = 'type.googleapis.com/google.actions.v2.DateTimeValueSpec'


class InterpretAs(object):
    CARDINAL = 'cardinal'
    ORDINAL = 'ordinal'
    CHARACTERS = 'characters'
    FRACTION = 'fraction'
    EXPLETIVE = 'expletive'
    BLEEP = 'bleep'
    UNIT = 'unit'
    VERBATIM = 'verbatim'
    SPELL_OUT = 'spell-out'
    DATE = 'date'
    TIME = 'time'
    TELEPHONE = 'telephone'


class BreakTimeUnit(object):
    MILLIS = 'ms'
    SECONDS = 's'


class BreakStrength(object):
    NONE = 'none'
    X_WEAK = 'x-weak'
    WEAK = 'weak'
    MEDIUM = 'medium'
    STRONG = 'strong'
    X_STRONG = 'x-strong'


class ProsodyRate(object):
    X_SLOW = "x-slow"
    SLOW = "slow"
    MEDIUM = "medium"
    FAST = "fast"
    X_FAST = "x-fast"
    DEFAULT = "default"


class ProsodyPitch(object):
    X_LOW = 'x-low'
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    X_HIGH = 'x-high'
    DEFAULT = 'default'


class EmphasisLevel(object):
    STRONG = 'strong'
    MODERATE = 'moderate'
    NONE = 'none'
    REDUCED = 'reduced'


class SimpleResponse(object):
    def __init__(self, speech=None, ssml=None, text=None):
        self.speech = speech
        self.ssml = ssml
        self.text = text

    def dict(self):
        item = {}
        if self.speech:
            item['textToSpeech'] = self.speech
        if self.ssml:
            item['ssml'] = self.ssml
        if self.text:
            item['displayText'] = self.text
        return item

    @staticmethod
    def get_simple_index(items):
        for index, item in enumerate(items):
            if 'simpleResponse' in item:
                return index
        return None

    def add(self, response):
        items = response.get_items()
        index = SimpleResponse.get_simple_index(items)
        item = {'simpleResponse': self.dict()}
        if index:
            items[index] = item
        else:
            items.append(item)


class Helper(object):
    @staticmethod
    def add_simple(response):
        items = response.get_items()
        index = SimpleResponse.get_simple_index(items)
        simple = SimpleResponse('~')
        if index:
            items[index] = {'simpleResponse': simple.dict()}
        else:
            simple.add(response)


class BasicCard(object):
    def __init__(self,
                 title=None, subtitle=None, text=None,
                 image=None, buttons=None, button=None,
                 image_display_options=None):
        self.title = title
        self.subtitle = subtitle
        self.formatted_text = text
        self.image = image
        if button:
            self.buttons = [button]
        elif buttons:
            self.buttons = buttons
        else:
            self.buttons = None
        self.image_display_options = image_display_options

    def dict(self):
        item = {}
        if self.title:
            item['title'] = self.title
        if self.subtitle:
            item['subtitle'] = self.subtitle
        if self.formatted_text:
            item['formattedText'] = self.formatted_text
        if self.image:
            item['image'] = self.image.dict()
        if self.buttons:
            b = []
            for button in self.buttons:
                b.append(button.dict())
            item['buttons'] = b
        if self.image_display_options:
            item['imageDisplayOptions'] = self.image_display_options.dict()
        return item

    def add(self, response):
        response.get_items().append({'basicCard': self.dict()})


class Image(object):
    def __init__(self, url, alt):
        self.url = url
        self.accessibility_text = alt

    def dict(self):
        return {'url': self.url, 'accessibilityText': self.accessibility_text}


class MediaObject(object):
    def __init__(self, name=None, description=None, url=None, icon=None, large_image=None):
        self.name = name
        self.description = description
        self.content_url = url
        self.large_image = large_image
        self.icon = icon

    def dict(self):
        item = {}
        if self.name:
            item['name'] = self.name
        if self.description:
            item['description'] = self.description
        if self.content_url:
            item['contentUrl'] = self.content_url
        if self.large_image:
            item['largeImage'] = self.large_image.dict()
        if self.icon:
            item['icon'] = self.icon.dict()
        return item


class MediaResponse(object):
    def __init__(self, media_type=MediaType.MEDIA_TYPE_UNSPECIFIED, media_object=None, media_objects=None):
        self.media_type = media_type
        if media_object:
            self.media_objects = [media_object]
        elif media_objects:
            self.media_objects = media_objects

    def dict(self):
        return {'mediaType': self.media_type, 'mediaObjects': [obj.dict() for obj in self.media_objects]}

    def add(self, response):
        response.get_items().append({'mediaResponse': self.dict()})


class AudioMediaResponse(MediaResponse):
    def __init__(self, name=None, description=None, url=None, icon=None, large_image=None):
        self.media_type = MediaType.AUDIO
        self.media_objects = [MediaObject(name=name,
                                          description=description, url=url, icon=icon, large_image=large_image)]


class Button(object):
    def __init__(self, title, url):
        self.title = title
        self.open_url_action = OpenUrlAction(url)

    def dict(self):
        return {'title': self.title, 'openUrlAction': self.open_url_action.dict()}


class OpenUrlAction(object):
    def __init__(self, url, android_app=None):
        self.url = url
        self.android_app = android_app

    def dict(self):
        item = {'url': self.url}
        if self.android_app:
            item['androidApp'] = self.android_app.dict()
        return item


class VersionFilter(object):
    def __init__(self, min_version=None, max_version=None):
        self.min_version = min_version
        self.max_version = max_version

    def dict(self):
        item = {}
        if self.min_version:
            item['minVersion'] = self.min_version
        if self.max_version:
            item['maxVersion'] = self.max_version
        return item


class AndroidApp(object):
    def __init__(self, package_name, versions=None):
        self.package_name = package_name
        self.versions = versions

    def dict(self):
        item = {'packageName': self.package_name}
        if self.versions:
            item['versions'] = [version.dict() for version in self.versions]
        return item


class End(object):
    def __init__(self):
        pass

    def add(self, response):
        response.get_google_payload()['expectUserResponse'] = False


class ListItem(object):
    def __init__(self, key, title, description=None, image=None, synonyms=None):
        self.title = title
        self.description = description
        self.image = image
        self.key = key
        self.synonyms = synonyms

    def dict(self):
        option = {'key': self.key}
        if self.synonyms:
            option['synonyms'] = self.synonyms
        item = {'title': self.title,
                'description': self.description,
                'optionInfo': option}
        if self.image:
            item['image'] = self.image.dict()
        return item


class List(object):
    def __init__(self, title, items):
        self.title = title
        self.items = items

    def dict(self):
        list = {'items': [item.dict() for item in self.items]}
        if self.title:
            list['title'] = self.title
        return {'intent': Intent.OPTION,
                'data': {
                    '@type': AtType.OPTION_VALUE_SPEC,
                    'listSelect': list}}

    def add(self, response):
        response.get_google_payload()['systemIntent'] = self.dict()


class CarouselItem(object):
    def __init__(self, title=None, description=None, image=None, option_info=None):
        self.title = title
        self.description = description
        self.image = image
        self.option_info = option_info


class Carousel(object):
    def __init__(self, items=None):
        self.items = items


class CarouselBrowseItem(object):
    def __init__(self, url, title, description=None, image=None, footer=None):
        self.title = title
        self.description = description
        self.footer = footer
        self.image = image
        self.open_url_action = OpenUrlAction(url)

    def dict(self):
        item = {'title': self.title, 'openUrlAction': self.open_url_action.dict()}
        if self.description:
            item['description'] = self.description
        if self.footer:
            item['footer'] = self.footer
        if self.image:
            item['image'] = self.image.dict()
        return item


class CarouselBrowse(object):
    def __init__(self, items, image_display_options=None):
        self.items = items
        self.image_display_options = image_display_options

    def dict(self):
        item = {'items': [item.dict() for item in self.items]}
        if self.image_display_options:
            item['imageDisplayOptions'] = self.image_display_options
        return item

    def add(self, response):
        items = response.get_items()
        items.append({'carouselBrowse': self.dict()})


class ColumnProperties(object):
    def __init__(self, header, align):
        self.header = header
        self.horizontal_alignment = align

    def dict(self):
        return {'header': self.header, 'horizontalAlignment': self.horizontal_alignment}


class Cell(object):
    def __init__(self, text):
        self.text = text

    def dict(self):
        return {'text': self.text}


class Row(object):
    def __init__(self, cells, divider_after=False):
        self.cells = cells
        self.divider_after = divider_after

    def dict(self):
        return {'cells': [cell.dict() for cell in self.cells], 'dividerAfter': self.divider_after}


class TableCard(object):
    def __init__(self, title=None, subtitle=None, image=None, columns=None, rows=None, buttons=None):
        self.title = title
        self.subtitle = subtitle
        self.image = image
        self.column_properties = columns
        self.rows = rows
        self.buttons = buttons

    def dict(self):
        item = {}
        if self.title:
            item['title'] = self.title
        if self.subtitle:
            item['subtitle'] = self.subtitle
        if self.image:
            item['image'] = self.image.dict()
        if self.column_properties:
            item['columnProperties'] = [cps.dict() for cps in self.column_properties]
        if self.rows:
            item['rows'] = [row.dict() for row in self.rows]
        if self.buttons:
            item['buttons'] = [button.dict() for button in self.buttons]
        return item

    def add(self, response):
        response.get_items().append({'tableCard': self.dict()})


class Suggestion(object):
    def __init__(self, title):
        self.title = title

    def dict(self):
        return {'title': self.title}

    def add(self, response):
        rich = response.get_rich_response()
        key = 'suggestions'
        if key not in rich:
            rich[key] = []
        rich[key].append(self.dict())


class Suggestions(object):
    def __init__(self, *args):
        self.suggestions = [Suggestion(title) for title in args]

    def add(self, response):
        rich = response.get_rich_response()
        key = 'suggestions'
        if key not in rich:
            rich[key] = []
        for sug in self.suggestions:
            rich[key].append(sug.dict())


class LinkOutSuggestion(object):
    def __init__(self, name, url):
        self.destinationName = name
        self.open_url_action = OpenUrlAction(url)

    def dict(self):
        return {'destinationName': self.destinationName,
                'url': self.open_url_action.url,
                'openUrlAction': self.open_url_action.dict()}

    def add(self, response):
        response.get_rich_response()['linkOutSuggestion'] = self.dict()


class Permission(object):
    def __init__(self, context, permissions):
        if type(permissions) is not list:
            permissions = [permissions]
        self.permissions = permissions
        self.context = context

    def dict(self):
        return {'intent': Intent.PERMISSION,
                'data': {'@type': AtType.PERMISSION_VALUE_SPEC,
                         'optContext': self.context,
                         'permissions': self.permissions}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class HelperDateTime(object):
    def __init__(self, date_time_text, date_text, time_text):
        self.date_time_text = date_time_text
        self.date_text = date_text
        self.time_text = time_text

    def dict(self):
        return {'intent': Intent.DATETIME,
                'data': {'@type': AtType.DATE_TIME_VALUE_SPEC,
                         'dialogSpec': {
                             'requestDatetimeText': self.date_time_text,
                             'requestDateText': self.date_text,
                             'requestTimeText': self.time_text}}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class HelperSignIn(object):
    def __init__(self):
        pass

    def dict(self):
        return {'intent': Intent.SIGN_IN}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class HelperConfirmation(object):
    def __init__(self, question):
        self.question = question

    def dict(self):
        return {'intent': Intent.CONFIRMATION,
                'data': {'@type': AtType.CONFIRMATION_VALUE_SPEC,
                         'dialogSpec': {
                             'requestConfirmationText': self.question}}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class HelperPlace(object):
    def __init__(self, prompt, context):
        self.prompt = prompt
        self.context = context

    def dict(self):
        return {'intent': Intent.PLACE,
                'data': {'@type': AtType.PLACE_VALUE_SPEC,
                         'dialogSpec': {
                             'extension': {
                                 '@type': AtType.PLACE_DIALOG_SPEC,
                                 'requestPrompt': self.prompt,
                                 'permissionContext': self.context}}}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class Location(object):
    def __init__(self, coordinates=None, name=None, formatted_address=None, place_id=None):
        self.coordinates = coordinates
        self.name = name
        self.formatted_address = formatted_address
        self.place_id = place_id
        # TODO Other fields https://developers.google.com/actions/reference/rest/Shared.Types/Location


class HelperAndroidLink(object):
    def __init__(self, url, package, reason):
        self.url = OpenUrlAction(url=url, android_app=AndroidApp(package_name=package))
        self.reason = reason

    def dict(self):
        return {'intent': Intent.LINK,
                'data': {'@type': AtType.LINK_VALUE_SPEC,
                         'openUrlAction': self.url.dict(),
                         'dialogSpec': {
                             'requestLinkReason': self.reason}}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class HelperNewSurface(object):
    def __init__(self, context, notification_title, capabilities):
        self.context = context
        self.notification_title = notification_title
        if type(capabilities) is not list:
            capabilities = [capabilities]
        self.capabilities = capabilities

    def dict(self):
        return {'intent': Intent.NEW_SURFACE,
                'data': {'@type': AtType.NEW_SURFACE_VALUE_SPEC,
                         'context': self.context,
                         'notificationTitle': self.notification_title,
                         'capabilities': self.capabilities}}

    def add(self, response):
        Helper.add_simple(response)
        response.get_google_payload()['systemIntent'] = self.dict()


class Storage(object):
    def __init__(self, overwrite=False, **kwargs):
        self.overwrite = overwrite
        if overwrite is not None:
            self.dictionary = {}
            if kwargs is not None:
                for key, value in kwargs.items():
                    if value:
                        self.dictionary[key] = value
        else:
            self.dictionary = None

    def add(self, response, request=None):
        if not self.dictionary:
            response.get_google_payload()['resetUserStorage'] = True  # Does this work?
            self.dictionary = {}
        elif not self.overwrite:
            self.dictionary.update(request.get_storage())
        response.get_google_payload()['userStorage'] = json.dumps(self.dictionary)


class LatLng(object):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class TimeOfDay(object):
    def __init__(self, hours, minutes, seconds, nanos):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.nanos = nanos


class DateTime(object):
    def __init__(self, date, time):
        self.date = date
        self.time = time


class UserProfile(object):
    def __init__(self, display_name=None, given_name=None, family_name=None):
        self.display_name = display_name
        self.given_name = given_name
        self.family_name = family_name


class AppResponse(object):
    def __init__(self, items, app_request=None):
        items = flatten(items)
        if type(items) is tuple:
            items = list(items)
        elif type(items) is not list:
            items = [items]
        self.response = {
            'payload':
                {
                    'google': {
                        'expectUserResponse': True,
                        'richResponse': {
                            'items': []
                        }
                    }
                }
        }
        if app_request and app_request.is_intent(Intent.CANCEL):
            items.append(End())
        for item in items:
            if type(item) is str:
                SimpleResponse(item).add(self)
            elif type(item) is Storage:
                item.add(self, app_request)
            else:
                item.add(self)

    def get_google_payload(self):
        return self.response['payload']['google']

    def get_rich_response(self):
        return self.get_google_payload()['richResponse']

    def get_items(self):
        return self.get_rich_response()['items']

    def json(self):
        return json.dumps(self.response)


class AppRequest(object):
    def __init__(self, data, as_json=True):
        if as_json:
            self.data = json.loads(data)
        else:
            self.data = data

    def get_payload(self):
        return self.data['originalDetectIntentRequest']['payload']

    def get_query(self):
        return self.data['queryResult']['queryText']

    def get_data(self, storage_name, param_name):
        data = self.get_storage().get(storage_name, None)
        if data is None:
            data = self.get_param(param_name)
        return data

    def get_param(self, name, original=False):
        if original:
            name = name+'.original'
        try:
            params = [param for param in self.data['queryResult']['outputContexts']]
            params = [param['parameters'] for param in params]
            for param in params:
                if name in param:
                    return param[name]
        except KeyError:
            return None

    def has_all_params(self):
        try:
            return self.data['queryResult']['allRequiredParamsPresent']
        except KeyError:
            return False

    def has(self, capabilities):
        try:
            if type(capabilities) is not list:
                capabilities = [capabilities]
            surf = self.get_payload()['surface']
            return self.check_surface(surf, capabilities)
        except AttributeError or KeyError:
            return False

    def has_surface(self, capabilities):
        try:
            if type(capabilities) is not list:
                capabilities = [capabilities]
            surfaces = self.get_payload()['availableSurfaces']
            for surf in surfaces:
                if self.check_surface(surf, capabilities):
                    return True
            return False
        except AttributeError or KeyError:
            return False

    def check_surface(self, surf, capabilities):
        return sum([1 if m_cap == s_cap['name'] else 0
                    for m_cap in capabilities
                    for s_cap in surf['capabilities']]) == len(capabilities)

    def is_intent(self, intent):
        if self.is_dialogflow_event_name(intent) or \
           self.is_dialogflow_action(intent) or \
           self.get_input(intent):
                return True
        return False

    def get_input(self, intent):
        try:
            inputs = self.get_payload()['inputs']
            for inp in inputs:
                if inp['intent'] == intent:
                    return inp
            return None
        except KeyError:
            return None

    def is_dialogflow_event_name(self, name):
        try:
            return self.data['queryResult']['intent']['displayName'] == name
        except KeyError:
            return False

    def is_dialogflow_action(self, action):
        try:
            return self.data['queryResult']['action'] == action
        except KeyError:
            return False

    def get_selected_option(self):
        inp = self.get_input(Intent.OPTION)
        return inp['arguments'][0]['textValue'] if inp else None

    def get_helper_date_time(self):
        inp = self.get_input(Intent.DATETIME)
        dt = inp['arguments'][0]['datetimeValue'] if inp else None
        if dt:
            date = dt['date']
            time = dt['time']
            return DateTime(date=Date(year=date.get('year'),
                                      month=date.get('month'),
                                      day=date.get('day')),
                            time=TimeOfDay(hours=time.get('hours'),
                                           minutes=time.get('minutes'),
                                           seconds=time.get('seconds'),
                                           nanos=time.get('nanos')))
        return None

    def has_permission(self):
        inp = self.get_input(Intent.PERMISSION)
        if inp:
            arg = inp['arguments'][0]
            try:
                return arg['textValue'] == 'true'
            except KeyError:
                return arg['boolValue']

    def get_permission_user_profile(self):
        try:
            user = self.get_payload()['user']['profile']
            return UserProfile(display_name=user.get('displayName'),
                               given_name=user.get('givenName'),
                               family_name=user.get('familyName'))
        except KeyError:
            return None

    def get_permission_location(self):
        try:
            coords = self.get_payload()['device']['location']['coordinates']
            return LatLng(latitude=coords['latitude'], longitude=coords['longitude'])
        except KeyError:
            return None

    def is_helper_signed_in(self):
        inp = self.get_input(Intent.SIGN_IN)
        return inp['arguments'][0]['extension']['status'] == 'OK'

    def get_helper_sign_in_access_token(self):
        return self.get_user().accessToken

    def get_helper_place(self):
        inp = self.get_input(Intent.PLACE)
        if inp:
            try:
                place = inp['arguments'][0]['placeValue']
                coords = place['coordinates']
                return Location(coordinates=LatLng(latitude=coords.get('latitude'), longitude=coords.get('longitude')),
                                name=place.get('name'),
                                formatted_address=place.get('formattedAddress'),
                                place_id=place.get('placeId'))
            except KeyError:
                return None
        else:
            return None

    def get_helper_confirmation(self):
        inp = self.get_input(Intent.CONFIRMATION)
        return inp['arguments'][0]['boolValue'] if inp else None

    def get_helper_link_status(self):
        inp = self.get_input(Intent.LINK)
        return inp['arguments'][0]['status']['code']

    def get_helper_new_surface(self):
        inp = self.get_input(Intent.NEW_SURFACE)
        return inp['arguments'][0]['extension']['status'] == 'OK'

    def get_storage(self):
        try:
            return json.loads(self.get_payload()['user']['userStorage'])
        except KeyError:
            return {}

    def json(self):
        return json.dumps(self.data)
