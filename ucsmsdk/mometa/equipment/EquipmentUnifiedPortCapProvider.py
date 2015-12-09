"""This module contains the general information for EquipmentUnifiedPortCapProvider ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class EquipmentUnifiedPortCapProviderConsts():
    INT_ID_NONE = "none"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"
    SUPPORTED_ALGORITHM_NONE = "none"
    SUPPORTED_ALGORITHM_SLIDE_RULE = "slide-rule"
    SUPPORTED_ALGORITHM_SLIDE_RULE_ETH_FIRST_DOUBLE_ROW = "slide-rule-eth-first-double-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_ETH_FIRST_SINGLE_ROW = "slide-rule-eth-first-single-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_3GFI_ROW = "slide-rule-fc-first-3gfi-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_DOUBLE_ROW = "slide-rule-fc-first-double-row"
    SUPPORTED_ALGORITHM_SLIDE_RULE_FC_FIRST_SINGLE_ROW = "slide-rule-fc-first-single-row"
    SUPPORTED_ALGORITHM_UNRESTRICTED = "unrestricted"


class EquipmentUnifiedPortCapProvider(ManagedObject):
    """This is EquipmentUnifiedPortCapProvider class."""

    consts = EquipmentUnifiedPortCapProviderConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentUnifiedPortCapProvider", "equipmentUnifiedPortCapProvider", "unified-port-cap", VersionMeta.Version201m, "InputOutput", 0xffL, [], [""], [u'equipmentGemCapProvider', u'equipmentSwitchCapProvider', u'equipmentSwitchIOCardCapProvider'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x4L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "end_port_id": MoPropertyMeta("end_port_id", "endPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "fc_speed_cap": MoPropertyMeta("fc_speed_cap", "fcSpeedCap", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((indeterminate|auto|defaultValue|1gbps|2gbps|16gbps|4gbps|8gbps),){0,7}(indeterminate|auto|defaultValue|1gbps|2gbps|16gbps|4gbps|8gbps){0,1}""", [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version201m, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x10L, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, 0x40L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "start_port_id": MoPropertyMeta("start_port_id", "startPortId", "uint", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version201m, MoPropertyMeta.READ_WRITE, 0x80L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "supported_algorithm": MoPropertyMeta("supported_algorithm", "supportedAlgorithm", "string", VersionMeta.Version201m, MoPropertyMeta.READ_ONLY, None, None, None, None, ["none", "slide-rule", "slide-rule-eth-first-double-row", "slide-rule-eth-first-single-row", "slide-rule-fc-first-3gfi-row", "slide-rule-fc-first-double-row", "slide-rule-fc-first-single-row", "unrestricted"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "endPortId": "end_port_id", 
        "fcSpeedCap": "fc_speed_cap", 
        "intId": "int_id", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "startPortId": "start_port_id", 
        "status": "status", 
        "supportedAlgorithm": "supported_algorithm", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.descr = None
        self.end_port_id = None
        self.fc_speed_cap = None
        self.int_id = None
        self.name = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.start_port_id = None
        self.status = None
        self.supported_algorithm = None

        ManagedObject.__init__(self, "EquipmentUnifiedPortCapProvider", parent_mo_or_dn, **kwargs)

