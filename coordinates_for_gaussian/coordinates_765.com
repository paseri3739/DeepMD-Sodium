%mem=12GB
%chk=checkpoint.chk
%nprocshared=16
#P B3LYP/6-311+g(d) force ! ASE formatted method and basis

Gaussian input prepared by ASE

0 1
Na                0.0000000000        3.1179852805        0.4329479932
Na                2.2348018159        4.9616529065        1.1897177715
Na                5.7763717565        1.8193209130        0.8798060310
Na                2.7893709543        2.0509674921        0.7097896329
Na                1.2663708603        2.9087134563        3.1478912655
Na                1.8555114021        0.0000000000        2.6895477081
Na                0.5403002361        0.1981319231        0.0000000000


