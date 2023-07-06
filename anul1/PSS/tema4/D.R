tconfidence=function(alfa,n,xn,devstandard){
  critical_t=qt(1-alfa/2,n-1)
  a=xn-critical_t*devstandard/sqrt(n)
  b=xn+critical_t*devstandard/sqrt(n)
  cat("Intervalul de incredere este: (",a,",",b,")\n")
}

cat("[Problema D1]\n")
D.zconfidence(1-0.95, 150,490,85*85)

cat("[Problema D2]\n")
D.zconfidence(1-0.99, 25,101.5,5*5)


D.testZProportions=function(alfa,n,succese,p0,tip_ipoteza){
  cat("Nivelul de seminificatie este",alfa,'\n')
  pprim=succese/n
  z_score=(pprim-p0)/(sqrt(p0*(1-p0)/n))
  if(tip_ipoteza=='l'){
    cat("Asimetrica la stanga:\n")
    critical_z=qnorm(alfa,0,1)
    if(z_score<critical_z){
      cat("Ipoteza nula este respinsa si accept ipoteza alternativa\n")
    }else{
      cat("Nu avem suficiente dovezi sa resping ipoteza nula")
    }
  }
  if(tip_ipoteza=='r'){
    cat("Asimetrica la dreapta:\n")
    critical_z=qnorm(1-alfa,0,1)
    if(z_score>critical_z){
      cat("Ipoteza nula este respinsa si accept ipoteza alternativa\n")
    }else{
      cat("Nu avem suficiente dovezi sa resping ipoteza nula")
    }
  }
  if(tip_ipoteza=='s'){
    cat("Simetrica :\n")
    critical_z=qnorm(1-alfa/2,0,1)
    if(abs(z_score)>abs(critical_z)){
      cat("Ipoteza nula este respinsa si accept ipoteza alternativa\n")
    }else{
      cat("Nu avem suficiente dovezi sa resping ipoteza nula")
    }
  }
  cat("\nZ_Score=",z_score,"\nZ critic=",critical_z,"\n")
}
#test_z=function(alfa,n,succese,p0,tip_ipoteza)
cat("[Problema D3 a)]\n")
D.testZProportions(0.01,1179,(1179*8.5)/100,0.08,'l')

cat("[Problema D3 b)]\n")
D.testZProportions(0.01,125,24,0.171,'l')
D.testZProportions(0.05,125,24,0.171,'l')

cat("[Problema D4)]\n")
D.testZProportions(0.01,250,95,0.4,'s')
D.testZProportions(0.05,250,95,0.4,'s')

