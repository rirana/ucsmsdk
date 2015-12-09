"""This module contains the general information for EquipmentUuidFeatureCap ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentUuidFeatureCapConsts():
    UUID_SUPPORT_MODE_LOOSE = "loose"
    UUID_SUPPORT_MODE_NONE = "none"
    UUID_SUPPORT_MODE_STRICT = "strict"


class EquipmentUuidFeatureCap(ManagedObject):
    """This is EquipmentUuidFeatureCap class."""

    consts = EquipmentUuidFeatureCapConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentUuidFeatureCap", "equipmentUuidFeatureCap", "uuid-feature-cap", VersionMeta.Version223a, "InputOutput", 0x1fL, [], ["read-only"], [u'equipmentBladeCapProvider', u'equipmentRackUnitCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "uuid_support_mode": MoPropertyMeta("uuid_support_mode", "uuidSupportMode", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, ["loose", "none", "strict"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "uuidSupportMode": "uuid_support_mode", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.sacl = None
        self.status = None
        self.uuid_support_mode = None

        ManagedObject.__init__(self, "EquipmentUuidFeatureCap", parent_mo_or_dn, **kwargs)

