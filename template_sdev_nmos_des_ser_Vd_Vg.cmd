

Device TWO_NMOS_DEV {

Electrode {
  { Name="source1"        Voltage=0.0 }
  { Name="drain1"         Voltage=0.0 }
  { Name="gate1"          Voltage=0.0 }
  { Name="substrate"      Voltage=0.0 }
  { Name="source2"        Voltage=0.0 }
  { Name="drain2"         Voltage=0.0 }
  { Name="gate2"          Voltage=0.0 }

}


File {
  * Input Files
  Grid      = "../two_nmos/two_nmos_new_msh.tdr"
  Parameter = "../two_nmos/models.par"
  * Output Files
  Current = "nmos_layout_#number#"
  Plot    = "nmos_layout_#number#"
  
}


**DopingDependence 

Physics{
  eQCvanDort 
  AreaFactor=1.0
  EffectiveIntrinsicDensity(BandGapNarrowing (OldSlotboom))
  Mobility (CarrierCarrierScattering DopingDependence   HighFieldsaturation    Enormal )
  Recombination ( SRH Auger )
     

**Strike on 1st NMOS
**This section is within Physics section
  HeavyIon (
  Direction=(0,1)  * y direction
  Location=(#xlocation#,#ylocation#)  *(x,y) micrometer point where the heavy ion enters the device
  Time=60e-12  ** Time at which the ion penetrates the device.
  Length=2.74  *track length in micron
  Wt_hi=0.35  *in microns
  LET_f=0.03  *in picoColoumb per micrometer
  Gaussian   *spatial distribution as a Gaussian function
  PicoCoulomb 	)
}

} *End TWO_NMOS_DEV device




File{
   Output = "log_global"
}


Plot{
*--Density and Currents, etc
   eDensity hDensity


*--Temperature 
*   eTemperature Temperature * hTemperature

*--Fields and charges
   ElectricField/Vector Potential SpaceCharge

*--Doping Profiles
   Doping DonorConcentration AcceptorConcentration

*--Generation/Recombination
   SRH Band2Band * Auger
 *  AvalancheGeneration eAvalancheGeneration hAvalancheGeneration

*--Driving forces
 *  eGradQuasiFermi/Vector hGradQuasiFermi/Vector
 *  eEparallel hEparallel eENormal hENormal

*--Band structure/Composition
   BandGap 
  * BandGapNarrowing
  * Affinity
  * ConductionBand ValenceBand
*   eQuantumPotential

*--Heavy Ion
  HeavyIonChargeDensity
  HeavyIonGeneration

}


System{



*Vdrain for NMOS
Vsource_pset drain_1 (drain1 0) { dc = #Vdrain1#}
Vsource_pset drain_2 (drain2 0) { dc = #Vdrain2#}

**Vin=Vgate
Vsource_pset vin (gate1 0) { dc = #Vgate1# }
Vsource_pset vin2 (gate2 0) { dc = #Vgate2# }

**Vsource
Vsource_pset vs (source1 0) { dc = #Vsource1# }
Vsource_pset vs2 (source2 0) { dc = #Vsource2# }

**Vsubstrate
Vsource_pset vsub (subs 0) { dc = 0}

TWO_NMOS_DEV two_nmos ( "source1"=source1  "drain1"=drain1 "gate1"=gate1 "substrate"=subs "source2"=source2  "drain2"=drain2 "gate2"=gate2 )

**Capacitor_pset cout ( drain2 0 ){ capacitance = 0.001e-12 }

Plot "nmos2_ser_layout_#number#.plt" (time() i(two_nmos,drain1) i(two_nmos,drain2) i(two_nmos,source1) i(two_nmos,source2))
 
  }  *End system



Math{
*  Extrapolate
*  RelErrControl
 * Digits=4
 * Notdamped=50
 * Iterations=12
 * Transient=BE
 * Method=Blocked
 * SubMethod=ParDiSo

 Extrapolate
 RelErrControl
*Newton iterations converge best with full derivatives.
Derivatives
notdamped=50 
 Iterations=20
*Improved Alpha Particle/Heavy Ion Generation RateIntegration
 RecBoxIntegr
*Parallel, iterative linear solver
 Method=ILS
* Spice_gmin=1e-15
Transient=BE
}


Solve
**This is the only sequential section in this command file
{  
  NewCurrentPrefix="init"
  Coupled(Iterations=30){ Poisson }
  Coupled{ Poisson Electron Hole Contact Circuit }



**Transient simulation

 NewCurrentPrefix=""
  Transient (
     InitialTime=0 FinalTime=400e-12
     InitialStep=1e-12 Increment=1.3
     MaxStep=5e-12 MinStep=1e-15
  ){ Coupled{ two_nmos.poisson two_nmos.electron two_nmos.hole two_nmos.contact 
           circuit }
  }

}



