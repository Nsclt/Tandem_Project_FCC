ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      DOUBLE PRECISION G
      COMMON/STRONG/ G

      DOUBLE COMPLEX GAL(2)
      COMMON/WEAK/ GAL

      DOUBLE PRECISION MU_R
      COMMON/RSCALE/ MU_R

      DOUBLE PRECISION NF
      PARAMETER(NF=4)

      DOUBLE PRECISION MDL_MT,MDL_MW,MDL_MZ,MDL_MTA,MDL_MB,MDL_MH

      COMMON/MASSES/ MDL_MT,MDL_MW,MDL_MZ,MDL_MTA,MDL_MB,MDL_MH


      DOUBLE PRECISION MDL_WZ,MDL_WH,MDL_WW,MDL_WT

      COMMON/WIDTHS/ MDL_WZ,MDL_WH,MDL_WW,MDL_WT


      DOUBLE COMPLEX GC_2, GC_3, GC_51, GC_58, GC_59, GC_100

      COMMON/COUPLINGS/ GC_2, GC_3, GC_51, GC_58, GC_59, GC_100

      DOUBLE COMPLEX CMASS_MDL_MH, CMASS_MDL_MZ, CMASS_MDL_MT,
     $  CMASS_MDL_MW

      COMMON/COMPLEX_MASS/ CMASS_MDL_MH, CMASS_MDL_MZ, CMASS_MDL_MT,
     $  CMASS_MDL_MW

