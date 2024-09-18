
#include <math.h>

  double add(double num1, double num2)
   {
    return num1+num2; //function returns multiplication of num1 and num2
   }
  double sub(double num1, double num2)
   {
    return num1-num2; //function returns multiplication of num1 and num2
   }
   double squar(double num1)
   {
    return pow(num1,2); //function returns multiplication of num1 and num2
   }
   double sq_rt(double num1)
   {
    return sqrt(num1); //function returns multiplication of num1 and num2
   }
   double mul(double num1, double num2)
   {
    return num1*num2; //function returns multiplication of num1 and num2
   }
   double div(double num1, double num2)
   {
    return num1/num2; //function returns multiplication of num1 and num2
   }

//Run the following commnad for generating the .so file
//cc -fPIC -shared -o funcs.so funcs.c
