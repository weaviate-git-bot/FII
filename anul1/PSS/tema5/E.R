# Tester pentru mediile Z
E.mediiZ=function(ipoteza,population_mean,dispersion,n,sample_mean,alfa,Z_score){
  #tip ipoteza as. la stg -> 'left'
  #            As. la dr-> 'right'
  #           Simetrica - > 'sim'
  sigma=sqrt(dispersion);
  if(missing(Z_score))
  {
    Z_score=(sample_mean-population_mean)/(sigma/sqrt(n));
  }
  if(ipoteza=='left'){
    critical_Z=qnorm(alfa,0,1)
    if(Z_score<critical_Z){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
  if(ipoteza=='right'){
    critical_Z=qnorm(1-alfa,0,1)
    if(Z_score>critical_Z){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
  if(ipoteza=='sim'){
    critical_Z=qnorm(1-alfa/2,0,1)
    if(abs(Z_score)>abs(critical_Z)){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
}
#Tester pentru mediile T
E.mediiT=function(ipoteza,population_mean,n,sample_mean,sigma,alfa, t_score){
  #tip ipoteza as. la stg -> 'left'
  #            As. la dr-> 'right'
  #           Simetrica - > 'sim'
  if(missing(t_score))
  {
    t_score=(sample_mean-population_mean)/(sigma/sqrt(n));
  }
  if(ipoteza=='left'){
    critical_t=qt(alfa,n-1)
    if(t_score<critical_t){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",t_score,"iar t critic:",critical_t,"\n")
  }
  if(ipoteza=='right'){
    critical_t=qt(1-alfa,n-1)
    if(t_score>critical_t){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",t_score,"iar t critic:",critical_t,"\n")
  }
  if(ipoteza=='sim'){
    critical_t=qt(1-alfa/2,n-1)
    if(abs(t_score)>abs(critical_t)){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",t_score,"iar t critic:",critical_t,"\n")
  }
  return(c(t_score,critical_t))
}


#Pentru z (ipoteza,population_mean,dispersion,n,sample_mean,alfa)
#Pentru t (ipoteza,population_mean,n,sample_mean,sigma,alfa)

# Problema 1
cat("[Problema E1]\n");
E.mediiT('left', 30,50,27,3.5,0.01)

cat("[Problema E2]\n");
E.mediiT('sim', 0,70,0,0,0.01,2.05)
E.mediiT('sim', 0,70,0,0,0.05,2.05)


# Probleme de medii
E.test_Z_dif_medii=function(ipoteza,m0,alfa,n1,n2,sample1,sample2,sigma1,sigma2){
  cat("Nivelul de seminificatie este de",alfa,"\n")
  #tip ipoteza as. la stg -> 'left'
  #            As. la dr-> 'right'
  #           Simetrica - > 'sim'
  Z_score=(sample1-sample2-m0)/sqrt((sigma1^2)/n1+(sigma2^2)/n2);
  if(ipoteza=='left'){
    critical_Z=qnorm(alfa,0,1)
    if(Z_score<critical_Z){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
  if(ipoteza=='right'){
    critical_Z=qnorm(1-alfa,0,1)
    if(Z_score>critical_Z){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
  if(ipoteza=='sim'){
    critical_Z=qnorm(1-alfa/2,0,1)
    if(abs(Z_score)>abs(critical_Z)){
      cat("Ipoteza nula este respinsa si se accepta ipoteza alternativa.\n")
    }else{
      cat("Nu avem suficiente dovezi pentru a respinge ipoteza nula si a accepta ipoteza alternativa.\n")
    }
    cat("Scorul este:",Z_score," Z critic: ",critical_Z,"\n")
  }
  return(c(critical_Z,Z_score))
}
#E.test_Z_dif_medii: (ipoteza,m0,alfa,n1,n2,sample1,sample2,sigma1,sigma2)

cat("[Problema E3]\n")
E.test_Z_dif_medii('left',0,0.01,200,224,7.8,8.1,1.15,0.92);
E.test_Z_dif_medii('left',0,0.05,200,224,7.8,8.1,1.15,0.92);
# In ambele cazuri se poate trage concluzia ca PhoneSkyGSM ofera servicii mai bune.

cat("[Problema E4]\n")
E.test_Z_dif_medii('right',0,0.01,50,50,102,109,8.3,7.5)

#Teste de tipul F
E.test_F_fisier=function(ipoteza,alfa,n1,n2,sigma1,sigma2){
  F_score=(sigma1^2)/(sigma2^2)
  if(ipoteza=='right'){
    critical_F=qf(1-alfa,n1-1,n2-1)
    if(F_score>critical_F){
      cat("Se accepta ipoteza alternativa.\n")
    }else{cat("Nu avem suficiente dovezi.\n")}
    cat("Fscore:",F_score," Fcritic: ",critical_F)
  }
  if(ipoteza == 'sim'){
    critical_Fs=qf(alfa/2,n1-1,n2-1)
    critical_Fd=qf(1-alfa/2,n1-1,n2-1)
    if((F_score<critical_Fs)||(F_score>critical_Fd)){
      cat("Se accepta ipoteza alternativa.\n")
    }else{cat("Nu avem suficiente dovezi.\n")}
    cat("Fscore:",F_score," Fscritic: ",critical_Fs," Fdcritic: ",critical_Fd)
  }
}

cat("[Problema E5]\n")
E.test_F_fisier('right', 0.01,22,22,2.15,1.95)



