import fir
# final = fir.fir("District", "year", "FIR_NO", "name", "dob", "date", "nationality", "nfotype", "P_Station", "time_period", "entry_no", "guardian_name", "address", "day", "complantant","others")
# final.ipc = [101,203]
# final.story = "vdcjdvh"
def write(final):
    with open("fir.txt","w") as f:
        string = f"Name = {final.name}\nDistrict = {final.District}\nyear = {final.year}\nFIR_NO = {final.FIR_NO}\nDate of birth = {final.dob}\nNationality = {final.nationality}\nInformation type = {final.infotype}\nPolice Station = {final.P_Station}\nTime Period = {final.time_period}\nEntry Number = {final.entry_no}\nFather's or Husband's name = {final.guardian_name}\nAddress = {final.address}\nDay = {final.day}\nComplantant = {final.complantant}\nOther data = {final.others}\nIpcs = {final.ipc}\nStory = {final.story}"
        f.write(string)
# write(final)
