section .data
	;bloque de mensajes de opciones
	option1 db"a) Hola Mundo!!!", 0xA
	longitud1 	equ $ - option1
	option2 db"b) Feliz Dia del Amor y las Amistad!!!", 0xA
	longitud2 	equ $ - option2
	option3 db"c) Feliz navidad!!!", 0xA
	longitud3 	equ $ - option3
	option4 db"d) Feliz Dia de la Independencia", 0xA
	longitud4 	equ $ - option4
	option5 db"e) otro(ingrese su propio mensaje)", 0xA
	longitud5 	equ $ - option5
	option6 db"f) finalizar el programa", 0xA
	longitud6	equ $ - option6
	
	;bloque de mensaje de las opciones
	mensaje1 db"Hola Mundo!!!", 0xA
	longitudM1 	equ $ - mensaje1
	mensaje2 db"Feliz Dia del Amor y las Amistad!!!", 0xA
	longitudM2 	equ $ - mensaje2
	mensaje3 db"Feliz navidad!!!", 0xA
	longitudM3 	equ $ - mensaje3
	mensaje4 db"Feliz Dia de la Independencia", 0xA
	longitudM4 	equ $ - mensaje4
	mensaje5 db"ingrese su propio mensaje", 0xA
	longitudM5 	equ $ - mensaje5
	mensaje6 db"finalizar el programa", 0xA
	longitudM6	equ $ - mensaje6
	
section .bss
    opcion resb 2  ;se crea variable para almacenar las opcion con tamaño de 2 bits
    mensaje resb 256 ;se crea variable para almacenar mensaje con un tamaño de 256 bits

section .text
	global _start
	
_start:

 menu_loop:;label del menu
		;primer opcion
		mov rdx, longitud1	;se carga la longitud	
		mov rcx, option1	;se carga el opcion a imprimir
		mov rbx, 1				
		mov rax, 4 				
		int 0x80
		
		;segundo opcion
		mov rdx, longitud2		;se carga la longitud
		mov rcx, option2		;se carga el opcion a imprimir
		mov rbx, 1				
		mov rax, 4 				
		int 0x80		
		
		mov rdx, longitud3;se carga la longitud
		mov rcx, option3	;se carga el opcion a imprimir
		mov rbx, 1
		mov rax,4
		int 0x80			
		
		mov rdx,longitud4;se carga la longitud
		mov rcx, option4;se carga el opcion a imprimir
		mov rbx, 1
		mov rax, 4
		int 0x80
		
		mov rdx, longitud5;se carga la longitud
		mov rcx, option5;se carga el opcion a imprimir
		mov rbx,1
		mov rax,4
		int 0x80
		
		mov rdx, longitud6;se carga la longitud
		mov rcx, option6;se carga el opcion a imprimir
		mov rbx,1
		mov rax,4
		int 0x80
		
		;se lee la opcion y se almacena
		mov rax, 3 ; se hace llamada a read
		mov rbx, 0 ; se establece en stadin
		mov	rcx, opcion ;se selecciona la variable
		mov rdx, 22
		int 0x80
		
		
		
		mov al, [opcion] ;se pasa el primer byte a al
		cmp al, 'a'      ;se compara con las distintas opciones  
		je opcion1 ;interrumpe el programa de manera condicional y carga el label de la opciob
		cmp al, 'b'             
		je opcion2;interrumpe el programa de manera condicional y carga el label de la opciob
		cmp al, 'c'             
		je opcion3;interrumpe el programa de manera condicional y carga el label de la opciob
		cmp al, 'd'
		je opcion4;interrumpe el programa de manera condicional y carga el label de la opciob
		cmp al, 'e'
		je opcion5;interrumpe el programa de manera condicional y carga el label de la opciob
		cmp al,'f'
		je salir;interrumpe el programa de manera condicional y carga el label de la opciob
		
		jmp menu_loop ;vuelve a cagar el label del menu si ninguna opcion es correcta
		
 opcion1:
		mov rdx, longitudM1	;se carga la longitud	
		mov rcx, mensaje1	;se carga el mensaje a imprimir	
		mov rbx, 1				
		mov rax, 4 				
		int 0x80
		jmp menu_loop ;vuelve al menu
 opcion2:
		mov rdx, longitudM2	;se carga la longitud	
		mov rcx, mensaje2	;se carga el mensaje a imprimir
		mov rbx, 1				
		mov rax, 4 				
		int 0x80
		jmp menu_loop;vuelve al menu
 opcion3:
		mov rdx, longitudM3	;se carga la longitud
		mov rcx, mensaje3	;se carga el mensaje a imprimir
		mov rbx, 1				
		mov rax, 4 				
		int 0x80
		jmp menu_loop;vuelve al menu
 opcion4:
		mov rdx, longitudM4	;se carga la longitud	
		mov rcx, mensaje4	;se carga el mensaje a imprimir
		mov rbx, 1				
		mov rax, 4 				
		int 0x80
		jmp menu_loop;vuelve al menu
 opcion5:
		mov rax, 4
		mov rbx, 1
		mov rcx, mensaje5 ;carga mensaje a imprimir
		mov rdx, longitudM5
		int 0x80
		
		mov rax, 3 ;se establece rax en read
		mov rbx, 0 
		mov	rcx, mensaje ;se elije variable para almacenar
		mov rdx, 256 ;se estable su largo 
		int 0x80
		
		mov rdx, 256 ;se da su largo
		mov rcx, mensaje
		mov rbx, 1
		mov rax,4 
		int 0x80
		jmp menu_loop ;carga el menu
 salir:
		mov rbx,0 ;establece pantalla en stadin para exit
		mov rax,1 ; se elige exit
		int 0x80 ; se interrupe el programa
	
