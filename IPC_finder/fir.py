class dateandtime:
    def __init__(self,date,time):
        self.date= date
        self.time = time
class place_of_occ:
    def __init__(self,distance_direction_from_PS,Beat_no,address,outside_limit):
        self.distance_direction_from_PS = distance_direction_from_PS
        self.Beat_no = Beat_no
        self.address = address
        self.outside_limit = outside_limit
class passp:
    def __init__(self,no,place,date):
        self.no = no
        self.place = place
        self.date = date
class identification:
    def __init__(self,no,typ):
        self.no = no
        self.typ = typ
class Complainant:
    def __init__(self,name,f_h_name,DOB,nationality,uid,passport,iid):
        self.name = name
        self.f_h_name = f_h_name
        self.DOB = DOB
        self.nationality = nationality
        self.uid = uid
        self.passport = passport
        self.iid = iid
class fir:
    def __init__(self, District, P_Station, FIR_NO, Time_Of_FIR, off_time_start, off_time_end, info_at_PS_time, diaryreff, infotype, place_of_occ,complantant):
        self.District = District
        self.P_Station = P_Station
        self.FIR_NO = FIR_NO
        self.Time_Of_FIR = Time_Of_FIR
        self.off_time_start = off_time_start
        self.off_time_end = off_time_end
        self.info_at_PS_time = info_at_PS_time
        self.diaryreff = diaryreff
        self.infotype = infotype
        self.place_of_occ = place_of_occ
        self.complantant = complantant

