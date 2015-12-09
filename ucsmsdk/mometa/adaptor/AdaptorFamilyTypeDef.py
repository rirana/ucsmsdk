"""This module contains the general information for AdaptorFamilyTypeDef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class AdaptorFamilyTypeDefConsts():
    IS_MULTI_PORT_FALSE = "false"
    IS_MULTI_PORT_NO = "no"
    IS_MULTI_PORT_TRUE = "true"
    IS_MULTI_PORT_YES = "yes"
    IS_PASSTHROUGH_FALSE = "false"
    IS_PASSTHROUGH_NO = "no"
    IS_PASSTHROUGH_TRUE = "true"
    IS_PASSTHROUGH_YES = "yes"
    IS_RETIMER_REQUIRED_FALSE = "false"
    IS_RETIMER_REQUIRED_NO = "no"
    IS_RETIMER_REQUIRED_TRUE = "true"
    IS_RETIMER_REQUIRED_YES = "yes"


class AdaptorFamilyTypeDef(ManagedObject):
    """This is AdaptorFamilyTypeDef class."""

    consts = AdaptorFamilyTypeDefConsts()
    naming_props = set([])

    mo_meta = MoMeta("AdaptorFamilyTypeDef", "adaptorFamilyTypeDef", "family-type", VersionMeta.Version202m, "InputOutput", 0x7ffL, [], ["read-only"], [u'adaptorFruCapProvider', u'equipmentLocalDiskControllerCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version202m, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "is_multi_port": MoPropertyMeta("is_multi_port", "isMultiPort", "string", VersionMeta.Version224b, MoPropertyMeta.READ_WRITE, 0x8L, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_passthrough": MoPropertyMeta("is_passthrough", "isPassthrough", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, None, ["false", "no", "true", "yes"], []), 
        "is_retimer_required": MoPropertyMeta("is_retimer_required", "isRetimerRequired", "string", None, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["false", "no", "true", "yes"], []), 
        "num_dce_ports": MoPropertyMeta("num_dce_ports", "numDcePorts", "uint", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "port_family": MoPropertyMeta("port_family", "portFamily", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x80L, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version202m, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version202m, MoPropertyMeta.READ_WRITE, 0x400L, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "isMultiPort": "is_multi_port", 
        "isPassthrough": "is_passthrough", 
        "isRetimerRequired": "is_retimer_required", 
        "numDcePorts": "num_dce_ports", 
        "portFamily": "port_family", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "type": "type", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.is_multi_port = None
        self.is_passthrough = None
        self.is_retimer_required = None
        self.num_dce_ports = None
        self.port_family = None
        self.sacl = None
        self.status = None
        self.type = None

        ManagedObject.__init__(self, "AdaptorFamilyTypeDef", parent_mo_or_dn, **kwargs)

