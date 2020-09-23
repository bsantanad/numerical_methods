/* false_pos -- 
 * a program that uses the false_position method to solve ecuations
 *
 * author: Benjamin Santana
 * date: 01/sept/2020
 *
 */

#include<stdio.h>
#include<math.h>

/* Write the function here*/
double f(double x){
    //return (13500/x)*(1.0-(1.0/pow(1+x, 240.0)))-1500000;
    //return 1800*log(160000/(160000-2600*x)) - 9.81*x - 750;
    //return x*cos(x)*sin(x);
    return pow(x,4) - 9*pow(x,3) - 169*pow(x,2) + 1101*x + 1260;
}
/* -------------------- */


int main(void){
   
    
    double xa = -5; 
    double xb = 2;

    int iter = 20;
    int i;
    double xc, fax, fbx, fcx;

  
    printf("|iter\t|\tx\t|\tf(x)\t|\n");
     
    fax = f(xa);
    fbx = f(xb);
    for(i=0; i<iter; i++){ 
	if(fax * fbx >= 0 && i==0){
	    printf("WARNING! f(xa) and f(xb) have the same sign!!\n");
	    break;
	}
	if(isnan(fax)) break;	
        
	//printf("|%d\t|%f\t|%f\t|\n",i, xa, fax);	
        xc = xb - ((fbx)*(xb-xa)/(fbx-fax));
	fcx = f(xc);
	
	if(fax*fcx<0){
	    xb = xc;
	    fbx = fcx;
	}else{
	    xa = xc;
	    fax = fcx; 	
	}

	printf("|%d\t|%f\t|%f\t|\n",i, xc, fcx);	
    }
   
    return 0;
}

