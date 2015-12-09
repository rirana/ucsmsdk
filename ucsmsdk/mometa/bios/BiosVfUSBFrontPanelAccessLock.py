"""This module contains the general information for BiosVfUSBFrontPanelAccessLock ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class BiosVfUSBFrontPanelAccessLockConsts():
    SUPPORTED_BY_DEFAULT_NO = "no"
    SUPPORTED_BY_DEFAULT_YES = "yes"
    VP_USBFRONT_PANEL_LOCK_DISABLED = "disabled"
    VP_USBFRONT_PANEL_LOCK_ENABLED = "enabled"
    VP_USBFRONT_PANEL_LOCK_PLATFORM_DEFAULT = "platform-default"
    VP_USBFRONT_PANEL_LOCK_PLATFORM_RECOMMENDED = "platform-recommended"


class BiosVfUSBFrontPanelAccessLock(ManagedObject):
    """This is BiosVfUSBFrontPanelAccessLock class."""

    consts = BiosVfUSBFrontPanelAccessLockConsts()
    naming_props = set([])

    mo_meta = MoMeta("BiosVfUSBFrontPanelAccessLock", "biosVfUSBFrontPanelAccessLock", "USB-Front-Panel-Access-Lock", VersionMeta.Version142b, "InputOutput", 0x3fL, [], ["admin", "ls-compute", "ls-config", "ls-server", "ls-server-policy", "pn-policy"], [u'biosSettings', u'biosVProfile'], [], ["Get", "Set"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version142b, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "prop_acl": MoPropertyMeta("prop_acl", "propAcl", "ulong", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version142b, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_by_default": MoPropertyMeta("supported_by_default", "supportedByDefault", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["no", "yes"], []), 
        "vp_usb_front_panel_lock": MoPropertyMeta("vp_usb_front_panel_lock", "vpUSBFrontPanelLock", "string", VersionMeta.Version142b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["disabled", "enabled", "platform-default", "platform-recommended"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "propAcl": "prop_acl", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "supportedByDefault": "supported_by_default", 
        "vpUSBFrontPanelLock": "vp_usb_front_panel_lock", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.prop_acl = None
        self.sacl = None
        self.status = None
        self.supported_by_default = None
        self.vp_usb_front_panel_lock = None

        ManagedObject.__init__(self, "BiosVfUSBFrontPanelAccessLock", parent_mo_or_dn, **kwargs)

