# Part of OpenG2P Registry. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Rest API",
    "category": "G2P",
    "version": "15.0.0.0.1",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/openg2p/openg2p-registry",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "maintainers": ["jeremi", "gonzalesedwin1123"],
    "depends": [
        "base",
        "mail",
        "contacts",
        "component",
        "base_rest",
        "base_rest_pydantic",
        "extendable",
        "g2p_registry_group",
        "g2p_registry_individual",
    ],
    "external_dependencies": {"python": ["extendable-pydantic", "pydantic"]},
    "data": [],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
