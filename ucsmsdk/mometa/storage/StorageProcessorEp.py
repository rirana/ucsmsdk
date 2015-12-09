"""This module contains the general information for StorageProcessorEp ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class StorageProcessorEpConsts():
    pass


class StorageProcessorEp(ManagedObject):
    """This is StorageProcessorEp class."""

    consts = StorageProcessorEpConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("StorageProcessorEp", "storageProcessorEp", "proc-ep-[name]", VersionMeta.Version302c, "InputOutput", 0x3fL, [], ["read-only"], [], [], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version302c, MoPropertyMeta.INTERNAL, 0x2L, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "ep_dn": MoPropertyMeta("ep_dn", "epDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version302c, MoPropertyMeta.NAMING, 0x8L, None, None, r"""[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "processor_dn": MoPropertyMeta("processor_dn", "processorDn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version302c, MoPropertyMeta.READ_WRITE, 0x20L, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "epDn": "ep_dn", 
        "name": "name", 
        "processorDn": "processor_dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.ep_dn = None
        self.processor_dn = None
        self.sacl = None
        self.status = None

        ManagedObject.__init__(self, "StorageProcessorEp", parent_mo_or_dn, **kwargs)

