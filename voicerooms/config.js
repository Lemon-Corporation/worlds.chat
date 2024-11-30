// Jitsi Meet configuration.
var config = {};

config.hosts = {};
config.hosts.domain = 'meet.jitsi';

var subdir = '<!--# echo var="subdir" default="" -->';
var subdomain = '<!--# echo var="subdomain" default="" -->';
if (subdir.startsWith('<!--')) {
    subdir = '';
}
if (subdomain) {
    subdomain = subdomain.substring(0,subdomain.length-1).split('.').join('_').toLowerCase() + '.';
}
config.hosts.muc = 'muc.' + subdomain + 'meet.jitsi';
config.bridgeChannel = {
    preferSctp: true
};

config.resolution = 720;
config.constraints = {
    video: {
        height: { ideal: 720, max: 720, min: 180 },
        width: { ideal: 1280, max: 1280, min: 320},
    }
};

config.startVideoMuted = 10;
config.startWithVideoMuted = false;

config.flags = {
    sourceNameSignaling: true,
    sendMultipleVideoStreams: true,
    receiveMultipleVideoStreams: true
};

config.enableNoAudioDetection = true;
config.enableTalkWhileMuted = false;
config.disableAP = false;

config.audioQuality = {
    stereo: false
};

config.startAudioOnly = false;
config.startAudioMuted = 10;
config.startWithAudioMuted = false;
config.startSilent = false;
config.enableOpusRed = false;
config.disableAudioLevels = false;
config.enableNoisyMicDetection = true;


// Peer-to-Peer options.
//

config.p2p = {
    enabled: true
};

config.toolbarButtons = [
   'camera',
   'fullscreen',
   'hangup',
   'microphone',
   'participants-pane',
   'raisehand',
   'settings',
   'tileview',
   'toggle-camera',
]

config.hideAddRoomButton = false;

config.localRecording = { disable: true };

config.analytics = {};


config.enableCalendarIntegration = false;

config.prejoinConfig = {
    enabled: false,
    hideDisplayName: false
};

config.welcomePage = {
    disabled: true
};

config.enableClosePage = false;

config.requireDisplayName = false;

config.disableProfile = false;

config.roomPasswordNumberOfDigits = false;

config.transcription = {
    enabled: false,
    translationLanguages: [],
    translationLanguagesHead: ['en'],
    useAppLanguage: true,
    preferredLanguage: 'en-US',
    disableStartForAll: false,
    autoCaptionOnRecord: false,
};

config.deploymentInfo = {};

config.disableDeepLinking = false;

config.videoQuality = {};
config.videoQuality.av1 = {};
config.videoQuality.h264 = {};
config.videoQuality.vp8 = {};
config.videoQuality.vp9 = {};

config.disableReactions = true;
config.disablePolls = true;

config.remoteVideoMenu = {
    disabled: false,
    disableKick: false,
    disableGrantModerator: false,
    disablePrivateChat: false
};

config.e2eping = {
    enabled: false
};

config.whiteboard = {
    enabled: false,
};

config.testing = {
    enableAv1Support: false
};
