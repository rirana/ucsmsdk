"""This module contains the general information for FabricNetflowMonExporterRef ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class FabricNetflowMonExporterRefConsts():
    SWITCH_ID_A = "A"
    SWITCH_ID_B = "B"
    SWITCH_ID_NONE = "NONE"


class FabricNetflowMonExporterRef(ManagedObject):
    """This is FabricNetflowMonExporterRef class."""

    consts = FabricNetflowMonExporterRefConsts()
    naming_props = set([u'nfMonExporterName'])

    mo_meta = MoMeta("FabricNetflowMonExporterRef", "fabricNetflowMonExporterRef", "flow-exporter-[nf_mon_exporter_name]", VersionMeta.Version221b, "InputOutput", 0x3fL, [], ["admin", "ext-lan-config", "ext-lan-policy"], [u'fabricNetflowMonitor'], [u'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version221b, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x2L, 0, 256, None, [], []), 
        "index": MoPropertyMeta("index", "index", "uint", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], ["0-2"]), 
        "nf_mon_exporter_name": MoPropertyMeta("nf_mon_exporter_name", "nfMonExporterName", "string", VersionMeta.Version221b, MoPropertyMeta.NAMING, 0x8L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "oper_nf_mon_exporter_name": MoPropertyMeta("oper_nf_mon_exporter_name", "operNfMonExporterName", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, 0x10L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version221b, MoPropertyMeta.READ_WRITE, 0x20L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "switch_id": MoPropertyMeta("switch_id", "switchId", "string", VersionMeta.Version221b, MoPropertyMeta.READ_ONLY, None, None, None, None, ["A", "B", "NONE"], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "index": "index", 
        "nfMonExporterName": "nf_mon_exporter_name", 
        "operNfMonExporterName": "oper_nf_mon_exporter_name", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "switchId": "switch_id", 
    }

    def __init__(self, parent_mo_or_dn, nf_mon_exporter_name, **kwargs):
        self._dirty_mask = 0
        self.nf_mon_exporter_name = nf_mon_exporter_name
        self.child_action = None
        self.index = None
        self.oper_nf_mon_exporter_name = None
        self.sacl = None
        self.status = None
        self.switch_id = None

        ManagedObject.__init__(self, "FabricNetflowMonExporterRef", parent_mo_or_dn, **kwargs)
