import typing
import protobug
from ._media_capabilities import MediaCapabilities


@protobug.message
class ClientAbrState:
    class MediaType(protobug.Enum):
        MEDIA_TYPE_DEFAULT = 0
        MEDIA_TYPE_AUDIO = 1
        MEDIA_TYPE_VIDEO = 2
        USE_SERVER_FORMAT_FILTER = 3

    time_since_last_manual_format_selection_ms: typing.Optional[protobug.Int32] = protobug.field(13, default=None)
    last_manual_direction: typing.Optional[protobug.Int32] = protobug.field(14, default=None)
    quality: typing.Optional[protobug.Int32] = protobug.field(16, default=None)
    detailed_network_type: typing.Optional[protobug.Int32] = protobug.field(17, default=None)
    max_width: typing.Optional[protobug.Int32] = protobug.field(18, default=None)
    max_height: typing.Optional[protobug.Int32] = protobug.field(19, default=None)
    selected_quality_height: typing.Optional[protobug.Int32] = protobug.field(21, default=None)
    unknown_field_22: typing.Optional[protobug.Int32] = protobug.field(22, default=None)  # seen on android = 1 (when playing audio+video only)
    r7: typing.Optional[protobug.Int32] = protobug.field(23, default=None)
    unknown_field_26: typing.Optional[protobug.Int32] = protobug.field(26, default=None)  # seen on android = 0
    unknown_field_27: typing.Optional[protobug.Int32] = protobug.field(27, default=None)  # seen on android = 5
    start_time_ms: typing.Optional[protobug.Int64] = protobug.field(28, default=None)
    time_since_last_seek: typing.Optional[protobug.Int64] = protobug.field(29, default=None)
    unknown_field_30: typing.Optional[protobug.Int32] = protobug.field(30, default=None)  # seen on android = 0
    unknown_field_32: typing.Optional[protobug.Int32] = protobug.field(32, default=None)  # seen on android = 0
    visibility: typing.Optional[protobug.Int32] = protobug.field(34, default=None)
    time_since_last_req: typing.Optional[protobug.Int64] = protobug.field(36, default=None)
    media_capabilities: typing.Optional[MediaCapabilities] = protobug.field(38, default=None)
    time_since_last_action: typing.Optional[protobug.Int64] = protobug.field(39, default=None)
    media_type: typing.Optional[MediaType] = protobug.field(40, default=None)
    player_state: typing.Optional[protobug.Int64] = protobug.field(44, default=None)
    range_compression: typing.Optional[protobug.Bool] = protobug.field(46, default=None)
    Jda: typing.Optional[protobug.Int32] = protobug.field(48, default=None)
    qw: typing.Optional[protobug.Int32] = protobug.field(50, default=None)
    Ky: typing.Optional[protobug.Int32] = protobug.field(51, default=None)
    sabr_report_request_cancellation_info: typing.Optional[protobug.Int32] = protobug.field(54, default=None)
    l: typing.Optional[protobug.Bool] = protobug.field(56, default=None)
    G7: typing.Optional[protobug.Int64] = protobug.field(57, default=None)
    prefer_vp9: typing.Optional[protobug.Bool] = protobug.field(58, default=None)
    qj: typing.Optional[protobug.Int32] = protobug.field(59, default=None)
    Hx: typing.Optional[protobug.Int32] = protobug.field(60, default=None)
    is_prefetch: typing.Optional[protobug.Bool] = protobug.field(61, default=None)
    sabr_support_quality_constraints: typing.Optional[protobug.Int32] = protobug.field(62, default=None)
    sabr_license_constraint: typing.Optional[protobug.Bytes] = protobug.field(63, default=None)
    allow_proxima_live_latency: typing.Optional[protobug.Int32] = protobug.field(64, default=None)
    sabr_force_proxima: typing.Optional[protobug.Int32] = protobug.field(66, default=None)
    Tqb: typing.Optional[protobug.Int32] = protobug.field(67, default=None)
    sabr_force_max_network_interruption_duration_ms: typing.Optional[protobug.Int64] = protobug.field(68, default=None)
    playback_rate: typing.Optional[protobug.Float] = protobug.field(285, default=None)
