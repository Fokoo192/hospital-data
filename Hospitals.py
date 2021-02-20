class Hospital:
    def __init__(self,name,num_icu_beds,occupied_beds,stretchers,masks,ventilator):
        self._name = name 
        self._num_icu_beds = num_icu_beds
        self._occupied_beds = occupied_beds
        self._stretchers = stretchers
        self._masks = masks
        self._ventilators = ventilator
        self._information = [self._num_icu_beds, self._occupied_beds,self._stretchers,self._masks,self._ventilators]

    #mutator methods 
    def set_icu_beds(self,num):
        self._num_icu_beds = num
    def set_occupied_beds(self,num):
        self._occupied_beds = num 
    def set_stretchers(self,num):
        self._stretchers = num
    def set_masks(self,num):
        self._masks = num 
    def set_ventilators(self,num):
        self._ventilators = num

    #accessor method
    def get_information(self):
        return self._information

    


