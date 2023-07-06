#Exercitul 1
B1 = function(N)
{
  correctCount =0;
  a=3;b=2;c=4;
  formula = (4*pi*a*b*c)/3;
  for(i in 1:N)
  {
    x = runif(1, -3,3);
    y = runif(1, -2,2);
    z = runif(1,-4,4);
    if(((x*x)/(a*a)+(y*y)/(b*b)+(z*z)/(c*c))<=1)
        correctCount=correctCount+1;
  }
  volume = (2*a)*(2*b)*(2*c);
  return (volume*correctCount/N);
}

a=3;b=2;c=4;
formula = (4*pi*a*b*c)/3;
cat("Volumul real este",formula,'\n');

runs = c(10000,20000,50000);
for(i in 1:length(runs))
{
  run = B1(runs[i]);
  eRel = abs(formula-run)/abs(formula);
  cat("Valoarea esantionului",runs[i],"este de",run,"avand o eroare de",eRel,"\n");
}

# Exercitiul 2
B2 = function(N)
{
  correctCount = 0;
  for(i in 1:N)
  {
    x = runif(1, 0, 2);
    y = runif(1, 0, 4);
    if(y<=x && 2*x+y<=4)
    {
      correctCount = correctCount+1;
    }
  }
  return (correctCount*4/N);
}

data = B2(50000);
cat("Aria estimata este",data,'\n')

# Exercitiul 3

B3.punctulA = function(N)
{
  val = 2-2*log(2);
  sum=0;
  for(i in 1:N)
  {
    x=runif(1, 0,1);
    sum = sum+ 1/(1+sqrt(x));
  }
  cat("Estimarea pentru integrala de la [0,1] din 1/(1+sqrt(x)) a fost",sum/N,"valoarea adevarata este",val,'\n');
  
}

B3.punctulA(50000)

B3.punctulB = function(a,N)
{
  val = pi/2;
  sum = 0;
  for(i in 1:N)
  {
    x=runif(1, 0, a);
    sum = sum+1/(1+x*x);
  }
  cat("Estimarea pentru integrala de la [0,",a,"] din 1/(1+x^2) a fost",(a-1)*sum/N,"valoarea adevarata este",val,'\n');
}
B3.punctulB(100,50000)

# Problema 4
B4.generateRequest = function(){
  done = 0;
  value = 0;
  while(done==0)
  {
    done = 1;
    x = runif(1, 0,1);
    if(x<=0.35)
    {
      value = dgamma(5,3)
    }else if(x<=0.50){
      value = dgamma(5,2)
    }else if(x<=0.70)
    {
      value = dgamma(4,3)
    }else{
      done = 0;
    }
  }
  value = value + pexp(4)
  return (value);
}

B4.mediumTime = function(N)
{
  sum = 0;
  for(i in 1:N)
  {
    sum = sum+B4.generateRequest()
  }
  cat("Timpul mediu dupa",N,"incercari este",sum/N,"milisecunde\n") 
}


B4.mediumTime(50000)


# Problema B5
B5.virusExpand = function(computers,infection_rate)
{
  for(idx in 1:(length(computers)-1))
  {
    if(computers[idx]==TRUE)
    {
      for(i in (idx+1):length(computers))
      {
        if(computers[i]==FALSE)
        {
          prob = runif(1,0,1);
          if(prob<=infection_rate)
            computers[i]=TRUE;
          
        }
      }
    }
  }
  return (computers)
}
B5.virusCured = function(computers,computers_to_be_healed,heal_rate)
{
  cured=0;
  healList = vector();
  availableToBeHealed = 0;
  #extract all
  for(i in 1:length(computers))
  {
    if(computers[i]==TRUE)
    {
      healList = c(healList, i);
    }
  }

  for(i in 1:length(healList))
  {
    x = runif(1,0,1)
    if(x<=heal_rate)
    {
      computers[healList[i]]=FALSE;
    }
  }
  
  return (computers)
}
B5.countInfectedComputers = function(computers)
{
  inf = 0
  for(i in 1:length(computers))
      if(computers[i]==TRUE)
          inf = inf+1;
  return (inf)
}
B5.initiateComputer = function(computerCount)
{
  vec = c(TRUE,TRUE,TRUE)
  for(i in 4:computerCount)
  {
    vec[i]=FALSE;
  }
  return (vec)
}
B5.initiateVirus = function(p,q,k)
{
  computerCount = 20;
  computers = B5.initiateComputer(computerCount);
  infection_rate = p;
  computers_to_be_healed = k;
  heal_rate = q;
  infectedComputers = 3;
  days = 1;
  while(infectedComputers > 0)
  {
      days=days+1;
      computers = B5.virusExpand(computers,infection_rate);
      computers = B5.virusCured(computers,computers_to_be_healed,heal_rate);
      infectedComputers = B5.countInfectedComputers(computers);
      #if it takes more than 100 is impossible!
      if(days>36524)
        return (-1)
  }
  return (days);
}

B5.punctulA = function(p,q,k,N)
{
  days = 0;
  for(i in 1:N)
    days = days+B5.initiateVirus(p,q,k);
  cat("Numarul mediu de zile pentru",N,"rulari este de",days/N," zile\n")
}
B5.punctulA(0.6, 0.55, 10,100);

B5.punctulB = function(p,q,k,N)
{
  days10 = 0;
  for(i in 1:N)
  {
    if(B5.initiateVirus(p,q,k)>=10)
        days10=days10+1;
  }
  cat("Probabilitatea ca dupa 10 zile sa mai existe calculatoare infectate este de", days10/N,"\n")
  return (days10/N)
}
prob = B5.punctulB(0.6, 0.55, 10,100);

B5.punctulC = function(prob, epsilon, p)
{
  alfa = 1-prob;
  z=qnorm(alfa/2);
  N_min = (p*(1-p)*(z/epsilon)^2);
  return (N_min);
}

probCuEroare = B5.punctulC(prob, 0.01,0.95)
cat("Folosind valoarea prezumata\n")
B5.punctulB(0.6,0.55,10,probCuEroare)




