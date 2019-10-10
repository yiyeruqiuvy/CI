#include<stdio.h>
#include<math.h>
float T = 1,l = 0.9;//21组作业，贡献度： 裴乾锋，毛梓蒙，王航 = 4:3:3
int main(){
	float f_c_w(float w1,float w2,float w3,float o[3],float st);
	float f_o(float o);
	float f_E_1(float o,float w,float e);//计算前面的节点误差
	float f_E_2(float o,float n);//计算输出节点的误差，即所求误差
	float f_w(float w_o,float o_o,float e);
	float f_st(float st,float e);
	int k = 0,i,j;
	float w_o[8] = {0.2, 0.4, -0.5, -0.3, 0.1, 0.2, -0.3, -0.2},w_n[8];
	float o_o[3] = {1, 0, 1}, o_n[3],E[3],n;//n为系数,0_0为123节点,0_n为456节点输入，
	float st_o[3] = {-0.4, 0.2, 0.1},st_n[3];//偏置
	while(k < 300){ //300次更迭
		//计算新的输出值456节点
		for(i = 0,j = 0;i < 3;i++,j+=3){
			if(i < 2){
				o_n[i] = f_o(f_c_w(w_o[j],w_o[j+1],w_o[j+2],o_o,st_o[i]));
			}
			else{
				o_n[i] = f_o(w_o[j]*o_n[i-2]+w_o[j+1]*o_n[i-1]+st_o[2]);
			}	
		}

		//计算误差
		E[2] = f_E_2(o_n[2],T);
		for(i = 0;i < 2;i++){
			E[i] = f_E_1(o_n[i],w_o[i+6],E[2]);
		}

		//计算新的节点输入
		i = 0;
		while(i < 8)
		{
			for (j = 0; j < 3;j++)
			{
				w_n[i] = f_w(w_o[i],o_o[j],E[j]);
				i++;
				if(j == 3)
				{
					j = -1;
				}
				if(i >= 6)
				{
					for (int m = 0; m < 2;m++)
					{
						w_n[i] = f_w(w_o[i],o_n[m],E[2]);
						i++;
					}
					break;
				}
			}
		}

		//计算新的st
		for(i = 0;i < 3;i++){
			st_n[i] = f_st(st_o[i],E[i]);
		}


		//替换，新换旧，即更新数据
		for(i = 0;i < 8;i++){
			w_o[i] = w_n[i];
		}
		for(i = 0;i < 3;i++){
			st_o[i] = st_n[i];
		}
		for(i = 0,j = 0;i < 3;i++,j+=3){
			if(i < 2){
				o_n[i] = f_o(f_c_w(w_o[j],w_o[j+1],w_o[j+2],o_o,st_o[i]));
			}
			else{
				o_n[i] = f_o(w_o[j]*o_n[i-2]+w_o[j+1]*o_n[i-1]+st_o[2]);
			}	
		}
		k++;
	}

//显示
	printf("新计算的值：\n");
	for (int i = 0; i < 3; i++)
	{
		printf("%f,%f,%f\n", o_n[i],E[i],st_n[i]);
	}
	printf("\n计算输出值：O=%f\n", o_n[2]);
	printf("更新的值：\n");
	for (int y = 0; y < 8; y++)
	{
		printf("%f||", w_n[y]);
	}

	return 0;
}
float f_c_w(float w1, float w2,float w3,float o[3], float st){
	return w1*o[0]+w2*o[1]+w3*o[2]+st;
}

float f_o(float o){
	return 1/(1+exp(-o));
}

float f_E_1(float o,float w,float e){
	return o*(1-o)*w*e;
}

float f_E_2(float o,float n){
	return o*(1-o)*(T-o);
}

float f_w(float w_o,float e,float o_o){
	return w_o+l*o_o*e;
}

float f_st(float st, float e){
	return st+l*e;
}




