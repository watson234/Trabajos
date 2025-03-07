section .data
		mensaje		db "hola mundo", 0xA
		longitud 	equ $ - mensaje
		
section .text
		global _inicio			;definimos el punto de entrada
		
_inicio:
		mov rdx, longitud		;EDX=long a imprimir
		mov rcx, mensaje		;ECX=cadena a impimir 
		mov rbx, 1				;EBX=manejador de fichero (STDOUT)
		mov rax, 4 				;EAX=función sys_write() del kernel
		int 0x80				;interrupc. 80 (llamada al kernel)
		
		mov rbx,0				;EBX=código de salida al 80
		mov rax,1				;EAX=función sys_exit() del kernel
		int 0x80				;interrupc. 80
