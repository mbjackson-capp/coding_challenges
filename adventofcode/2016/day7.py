import re

from aocd import get_data

input = get_data(year=2016, day=7).split("\n")

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def abbas_re() -> str:
    abbas = set()
    for idx, char1 in enumerate(ALPHABET):
        for char2 in ALPHABET[idx + 1 :]:
            abbas.add(f"{char1}{char2}{char2}{char1}")
            abbas.add(f"{char2}{char1}{char1}{char2}")
    return "|".join(sorted(abbas))


def aba_bab_setup() -> tuple[dict, str]:
    abas = set()
    aba_bab_lookup = {}
    for idx1, char1 in enumerate(ALPHABET):
        for idx2, char2 in enumerate(ALPHABET):
            if idx1 != idx2:
                aba = f"{char1}{char2}{char1}"
                bab = f"{char2}{char1}{char2}"
                abas.add(aba)
                aba_bab_lookup[aba] = bab
    return aba_bab_lookup, "|".join(sorted(abas))


ABBAS_RE = abbas_re()

HYPERNET_RE = r"\[[^\[\]]*\]"

ABA_BAB_LOOKUP, ABA_RE = aba_bab_setup()


def find_all_abas(ip: str) -> set[str]:
    abas = set()
    """Find all ABA pairs, allowing for overlap (unlike re.findall)"""
    for ix, _ in enumerate(ip):
        try:
            substring = ip[ix : ix + 3]
            if substring in ABA_BAB_LOOKUP:
                abas.add(substring)
        except IndexError:
            continue
    return abas


def supports_tls(ip: str) -> bool:
    ip_hypernet = "".join(re.findall(HYPERNET_RE, ip))
    ip_supernet = re.sub(HYPERNET_RE, "|", ip)
    return bool(re.findall(ABBAS_RE, ip_supernet) and not re.findall(ABBAS_RE, ip_hypernet))


def supports_ssl(ip: str) -> bool:
    ip_hypernet = "".join(re.findall(HYPERNET_RE, ip))
    ip_supernet = re.sub(HYPERNET_RE, "|", ip)
    supernet_abas = find_all_abas(ip_supernet)
    hypernet_abas = find_all_abas(ip_hypernet)
    for aba in supernet_abas:
        bab = ABA_BAB_LOOKUP[aba]
        if bab in hypernet_abas:
            return True
    return False


def run(input: list[str], condition_func):
    count = 0
    for ip in input:
        count += condition_func(ip)  # abuse python truthiness
    return count


if __name__ == "__main__":
    print(f"Part 1 answer: {run(input, supports_tls)}")
    print(f"Part 2 answer: {run(input, supports_ssl)}")
