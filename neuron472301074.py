'''
Defines a class, Neuron472301074, of neurons from Allen Brain Institute's model 472301074

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472301074:
    def __init__(self, name="Neuron472301074", x=0, y=0, z=0):
        '''Instantiate Neuron472301074.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472301074_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Pvalb-IRES-Cre_Ai14_IVSCC_-170931.06.01.01_464188986_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472301074_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 59.62
            sec.e_pas = -87.8744049072
        
        for sec in self.axon:
            sec.cm = 2.33
            sec.g_pas = 0.000460546063642
        for sec in self.dend:
            sec.cm = 2.33
            sec.g_pas = 1.63950793144e-06
        for sec in self.soma:
            sec.cm = 2.33
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.000129108
            sec.gbar_NaV = 0.0499665
            sec.gbar_Kd = 1.96164e-06
            sec.gbar_Kv2like = 0.000806978
            sec.gbar_Kv3_1 = 0.932027
            sec.gbar_K_T = 0.0123533
            sec.gbar_Im_v2 = 0.000230684
            sec.gbar_SK = 0.00213302
            sec.gbar_Ca_HVA = 0.000175702
            sec.gbar_Ca_LVA = 0.00873738
            sec.gamma_CaDynamics = 0.00299709
            sec.decay_CaDynamics = 37.1306
            sec.g_pas = 6.09891e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

