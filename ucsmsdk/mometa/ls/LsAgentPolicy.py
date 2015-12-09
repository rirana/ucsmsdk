"""This module contains the general information for LsAgentPolicy ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class LsAgentPolicyConsts():
    CAPABILITY_HOST_NAME_CONFIG = "host-name-config"
    CAPABILITY_L2_IF_CONFIG = "l2-if-config"
    CAPABILITY_L3_IF_CONFIG = "l3-if-config"
    CAPABILITY_STATES = "states"
    CAPABILITY_STATS = "stats"
    INT_ID_NONE = "none"
    MODE_FULL = "full"
    MODE_NO_AGENT = "no-agent"
    MODE_READ_ONLY = "read-only"
    POLICY_OWNER_LOCAL = "local"
    POLICY_OWNER_PENDING_POLICY = "pending-policy"
    POLICY_OWNER_POLICY = "policy"


class LsAgentPolicy(ManagedObject):
    """This is LsAgentPolicy class."""

    consts = LsAgentPolicyConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("LsAgentPolicy", "lsAgentPolicy", "agent-policy-[name]", VersionMeta.Version101e, "InputOutput", 0x3ffL, [], ["admin", "ls-config-policy", "ls-server-policy"], [u'orgOrg'], [], [None])

    prop_meta = {
        "capability": MoPropertyMeta("capability", "capability", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, ["host-name-config", "l2-if-config", "l3-if-config", "states", "stats"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x4L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "descr": MoPropertyMeta("descr", "descr", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8L, None, None, r"""[ !#$%&\(\)\*\+,\-\./:;\?@\[\]_\{\|\}~a-zA-Z0-9]{0,256}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "int_id": MoPropertyMeta("int_id", "intId", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, None, None, None, None, ["none"], ["0-4294967295"]), 
        "mode": MoPropertyMeta("mode", "mode", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["full", "no-agent", "read-only"], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x40L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "policy_level": MoPropertyMeta("policy_level", "policyLevel", "uint", VersionMeta.Version211a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "policy_owner": MoPropertyMeta("policy_owner", "policyOwner", "string", VersionMeta.Version211a, MoPropertyMeta.READ_WRITE, 0x80L, None, None, None, ["local", "pending-policy", "policy"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x100L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "capability": "capability", 
        "childAction": "child_action", 
        "descr": "descr", 
        "dn": "dn", 
        "intId": "int_id", 
        "mode": "mode", 
        "name": "name", 
        "policyLevel": "policy_level", 
        "policyOwner": "policy_owner", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.capability = None
        self.child_action = None
        self.descr = None
        self.int_id = None
        self.mode = None
        self.policy_level = None
        self.policy_owner = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "LsAgentPolicy", parent_mo_or_dn, **kwargs)

