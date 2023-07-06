A1.poisson = function(lambda, k, l)
{
  vec = k:(l-1);
  barplot(dpois(vec, lambda),legend.text="Distributia Poisson");
}

A1.geometric = function(lambda, k,l){
  vec = k:(l-1);
  barplot(dgeom(vec, lambda),legend.text="Distributia Geometrica");
}

A2.punctulA = function(fileName)
{
  vec = vector();
  dataSample = scan(fileName);
  vec[0] = median(dataSample);
  vec[1] = mean(dataSample);
  vec[2] = sd(dataSample);
  vec[3] = quantile(dataSample)[2];
  vec[4] = quantile(dataSample)[4];
  return (vec);
}

A2.punctulB = function(fileName)
{
  newData = vector();
  dataSample = scan(fileName);
  m = mean(dataSample);
  s = sd(dataSample);
  len = length(dataSample)
  for(i in 1:len)
  {
    if(!(dataSample[i]< m-2*s || dataSample[i]>m+2*s))
    {
      newData = c(newData, dataSample[i]);
    }
  }
  return (newData);
}

A3.punctulC = function(dataSample)
{
  print("Intervalele");
  intervals = seq(30, max(dataSample)+10,10);
  hist(dataSample, breaks=intervals, right=F, freq=T)
}

A3.punctulC(A2.punctulB('~/Documents/Work/UAIC/PSS/tema1/date.in'))



