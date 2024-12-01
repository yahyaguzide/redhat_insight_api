import difflib
import bisect


class RedHatHost:
    _id_fqdn_list: list[dict[str: any]] = []
    _id_hosts: dict[str: dict[str:any]] = {}

    def __init__(self, hosts: list[dict[str:any]]):
        for host in hosts:
            self._id_fqdn_list.append({"id": host["id"], "fqdn": host["fqdn"]})
            self._id_hosts[host["id"]] = host

    def get_id(self, index: int, *indexes: int) -> list[dict[str: any]]:
        index_list = [index] + list(indexes)
        return [self._id_fqdn_list[i] for i in index_list]

    def get_customer(self, index):
        pass

    def get_data(self, host_id: str) -> dict[str:any]:
        return self._id_hosts[host_id]

    def get_id_hosts(self) -> dict[str: dict[str:any]]:
        return self._id_hosts

    def get_fqdn_list(self) -> list[dict[str: any]]:
        return self._id_fqdn_list

    def get_hosts(self, host_id: str, *host_ids: str):
        host_id_list = list(host_id) + list(host_ids)
        tmp_list: list[any] = []
        for hid in host_id_list:
            tmp_list.append(self._id_hosts[hid])
        return tmp_list

    def search_fqdn(self, fqdn: str) -> list[dict[str:any]]:
        if fqdn == "":
            return self._id_fqdn_list

        tmp_list: list[any] = []
        for tmp_fqdn in self._id_fqdn_list:
            ratio: float
            if fqdn.lower() == tmp_fqdn["fqdn"].lower().strip():
                ratio = 1.0
            elif fqdn.lower() in tmp_fqdn["fqdn"].lower().strip():
                ratio = 0.9
            else:
                # This does work, but does not account for position
                # if searched for ad it will match a lot of systems even if the ratio is under 0.5
                ratio = difflib.SequenceMatcher(None, tmp_fqdn["fqdn"], fqdn).ratio()
            if ratio > 0.8:
                tmp_dict: dict[str: any] = {"ratio": ratio, "id": tmp_fqdn["id"], "fqdn": tmp_fqdn["fqdn"]}
                tmp_list.insert(bisect.bisect_left(tmp_list, ratio, key=lambda x: -1 * x["ratio"]), tmp_dict)
                if ratio == 1.0:
                    break

        #        for elem in tmp_list:
        #            del elem["ratio"]
        return tmp_list

    def search_id(self, hid: str) -> list[dict[str:any]]:
        if hid == "":
            return self._id_fqdn_list

        tmp_list: list[any] = []
        for tmp_fqdn in self._id_fqdn_list:
            ratio: float
            if hid.lower() == tmp_fqdn["id"].lower():
                ratio = 1.0
            elif hid.lower() in tmp_fqdn["id"].lower():
                ratio = 0.9
            else:
                # This does work, but does not account for position
                # if searched for ad it will match a lot of systems even if the ratio is under 0.5
                ratio = difflib.SequenceMatcher(None, tmp_fqdn["id"], hid).ratio()
            if ratio > 0.8:
                tmp_dict: dict[str: any] = {"ratio": ratio, "id": tmp_fqdn["id"], "fqdn": tmp_fqdn["fqdn"]}
                tmp_list.insert(bisect.bisect_left(tmp_list, ratio, key=lambda x: -1 * x["ratio"]), tmp_dict)
                if ratio == 1.0:
                    break

        #        for elem in tmp_list:
        #            del elem["ratio"]
        return tmp_list

