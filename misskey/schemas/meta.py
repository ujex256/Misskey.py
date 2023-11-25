import inspect
from dataclasses import dataclass
from typing import List

from marshmallow import Schema, fields, post_load

__all__ = (
    "MisskeyMeta",
    "MisskeyMetaSchema",
)


@dataclass
class MisskeyMeta:
    maintainer_name: str
    maintainer_email: str
    version: str
    name: str
    short_name: str
    uri: str
    description: str
    langs: List[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**{
            k: v for k, v in data.items()
            if k in inspect.signature(cls).parameters
        })


class MisskeyMetaSchema(Schema):
    maintainer_name = fields.String(
        required=True, allow_none=True, data_key="maintainerName")
    maintainer_email = fields.String(
        required=True, allow_none=True, data_key="maintainerEmail")
    version = fields.String(required=True)
    name = fields.String(required=True, allow_none=True)
    short_name = fields.String(
        required=True, allow_none=True, data_key="shortName")
    uri = fields.Url(required=True)
    description = fields.String(required=True, allow_none=True)
    langs = fields.List(fields.String(), required=True)
    tos_url = fields.String(required=True, allow_none=True, data_key="tosUrl")
    repository_url = fields.String(required=True, data_key="repositoryUrl")
    feedback_url = fields.String(required=True, data_key="feedbackUrl")
    default_dark_theme = fields.String(
        required=True, allow_none=True, data_key="defaultDarkTheme")
    default_light_theme = fields.String(
        required=True, allow_none=True, data_key="defaultLightTheme")
    disable_registration = fields.Boolean(
        required=True, data_key="disableRegistration")
    cache_remote_files = fields.Boolean(
        required=True, data_key="cacheRemoteFiles")
    cache_remote_sensitive_files = fields.Boolean(
        required=True, data_key="cacheRemoteSensitiveFiles")
    email_required_for_signup = fields.Boolean(
        required=True, data_key="emailRequiredForSignup")
    enable_hcaptcha = fields.Boolean(required=True, data_key="enableHcaptcha")
    hcaptcha_site_key = fields.String(
        required=True, allow_none=True, data_key="hcaptchaSiteKey")
    enable_recaptcha = fields.Boolean(
        required=True, data_key="enableRecaptcha")
    recaptcha_site_key = fields.String(
        required=True, allow_none=True, data_key="recaptchaSiteKey")
    enable_turnstile = fields.Boolean(
        required=True, data_key="enableTurnstile")
    turnstile_site_key = fields.String(
        required=True, allow_none=True, data_key="turnstileSiteKey")
    sw_public_key = fields.String(
        required=True, allow_none=True, data_key="swPublicKey")
    mascot_image_url = fields.String(
        required=True, data_key="mascotImageUrl")
    banner_url = fields.String(required=True, data_key="bannerUrl")
    server_error_image_url = fields.String(
        required=True, allow_none=True, data_key="serverErrorImageUrl")
    info_image_url = fields.String(
        required=True, allow_none=True, data_key="infoImageUrl")
    not_found_image_url = fields.String(
        required=True, allow_none=True, data_key="notFoundImageUrl")
    icon_url = fields.String(
        required=True, allow_none=True, data_key="iconUrl")
    max_note_text_length = fields.Integer(
        required=True, data_key="maxNoteTextLength")
    # ads = fields.List(...  # TODO: TBD
    notes_per_one_ad = fields.Integer(
        required=True, default=0, data_key="notesPerOneAd")
    require_setup = fields.Boolean(required=True, data_key="requireSetup")
    enable_email = fields.Boolean(required=True, data_key="enableEmail")
    enable_service_worker = fields.Boolean(
        required=True, data_key="enableServiceWorker")
    translator_available = fields.Boolean(
        required=True, data_key="translatorAvailable")
    proxy_account_name = fields.String(
        required=True, allow_none=True, data_key="proxyAccountName")
    media_proxy = fields.String(
        required=True, data_key="mediaProxy")
    # features = fields.Nested(...  # TODO: TBD

    # noinspection PyUnusedLocal
    @post_load()
    def load_schema(self, data, **kwargs):
        return MisskeyMeta.from_dict(data)
