from Diplomacy import EtiquetteInfo


class PoliteName:
    _first_name = str()
    _middle_name = str()
    _last_name = str()
    # для потомков
    for descendants GetPoliteFirstName: lambda EtiquetteInfo -> str:...
    for descendants GetPoliteMiddleName: lambda EtiquetteInfo -> str:...
    for descendants GetPoliteLastName: subprogram with (EtiquetteInfo) parameters returns String,
    @classmethod
    def GetFullName(EtiquetteInfo) -> str:
        ...

def GetPoliteFirstName.PoliteName(EtiquetteInfo _EtiquetteInfo) parameters returning String implemented as
    return _EtiquetteInfo.PoliteFirstName(FirstName).

def GetPoliteMiddleName.PoliteName(EtiquetteInfo _EtiquetteInfo) parameters returning String implemented as
    return _EtiquetteInfo.PoliteMiddleName(MiddleName).

def GetPoliteLastName(EtiquetteInfo _EtiquetteInfo) parameters returning String implemented as
    return _EtiquetteInfo.PoliteLastName(LastName).

def GetFullName(EtiquetteInfo _EtiquetteInfo) parameters returning String implemented as
    return GetPoliteFirstName(_EtiquetteInfo) + GetPoliteMiddleName(_EtiquetteInfo) 
        + GetPoliteLastName(_EtiquetteInfo).