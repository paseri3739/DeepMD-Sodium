%NProcShared=16
%mem=12GB
%Chk=checkpoint.chk
#p B3LYP/6-311+g(d) force

Test

0 1
Na    0.0    0.0    0.0
Na    0.0    0.0    4.7381695124505985
Na    0.0    0.0    8.001657739517373
Na    0.0    0.0    12.043230007449829

--Link1--
%NProcShared=16
%mem=12GB
%Chk=checkpoint.chk
#p B3LYP/6-311+g(d) force

Test

0 1
Na    0.0    0.0    0.0
Na    0.0    0.0    2.344257634429043
Na    0.0    0.0    6.398739122941146
Na    0.0    0.0    10.262636292911996

--Link1--
%NProcShared=16
%mem=12GB
%Chk=checkpoint.chk
#p B3LYP/6-311+g(d) force

Test

0 1
Na    0.0    0.0    0.0
Na    0.0    0.0    5.144117623859537
Na    0.0    0.0    9.524374494509651
Na    0.0    0.0    15.01150029067006
