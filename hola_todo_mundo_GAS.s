.data
        opcion: .space 20 @se crea variable con espacio de 20 bits
	mensajeU: .space 256 @se establece variable para alamacenar el mensaje
    @bloque de mensajes de opciones

        opt1: .asciz "a)Hola Mundo!!!\n"
        opt2: .asciz "b)Feliz Dia del Amor y la Amistad\n"
        opt3: .asciz "c)Feliz Navidad!!!\n"
        opt4: .asciz "d)Feliz Dia de la independencia!!!\n"
        opt5: .asciz "e)Otro(ingrese su propio mensaje)\n"
        opt6: .asciz "f)Salir\n"

        @bloque de mensajes
        msg1: .asciz "Hola Mundo!!!\n"
        msg2: .asciz "Feliz Dia del Amor y la Amistad\n"
        msg3: .asciz "Feliz Navidad!!!\n"
        msg4: .asciz "Feliz Dia de la independencia!!!\n"
	msg5: .asciz "ingrese mensaje\n"
.text
        .global _start
_start:push {r7, lr}
        b menu @se carga label de menu
menu:
        @se carga primer opcion
        mov r0,#1
        ldr r1,=opt1
        mov r2,#17
        mov r7,#4
        swi #0

        @se carga segunda opcion
        mov r0,#1
        ldr r1,=opt2
        mov r2,#34
        mov r7,#4
        swi #0

        @se carga tercer opcion
        mov r0,#1
        ldr r1,=opt3
        mov r2,#22
        mov r7,#4
	    swi #0

       @se carga cuarto opcion
        mov r0,#1
        ldr r1,=opt4
        mov r2,#35
        mov r7,#4
        swi #0

        @se carga quinta opcion
        mov r0,#1
        ldr r1,=opt5
        mov r2,#35
        mov r7,#4
        swi #0

        @se carga sexta opcion
        mov r0,#1
        ldr r1,=opt6
        mov r2,#8
        mov r7,#4
        swi #0

        @bloque para leer la opcion 
        mov r0,#0 
        ldr r1, =opcion @se establece la variable de almacenar la opcion
        mov r2, #20 @se da el largo de bytes
        mov r7, #3  @se establece la opcion en read
        swi #0

        ldr r1, =opcion @se carga la opcion a r1
        ldrb r1, [r1] @se elije solo el primer byte

        cmp r1, #'a' 
	beq mensaje1 @condicional para cambiar de label
	cmp r1, #'b'
	beq mensaje2 @condicional para cambiar de label
	cmp r1, #'c'
	beq mensaje3 @condicional para cambiar de label
	cmp r1, #'d'
	beq mensaje4 @condicional para cambiar de label
	cmp r1, #'e'
	beq mensaje5 @condicional para cambiar de label
	cmp r1, #'f'
	beq salir   @condicional para cambiar de label

	b menu @se carga label de menu si ninguan opcion es correcta
mensaje1: @primer label de mensajes
	mov r0,#1
	ldr r1,=msg1
	mov r2,#15
	mov r7,#4
	swi #0

	b menu  @se carga label de menu

mensaje2:@segundo label de mensajes
	mov r0,#1
	ldr r1,=msg2
	mov r2,#33
	mov r7,#4
	swi #0

	b menu   @se carga label de menu

mensaje3:@tercer label de mensajes
	mov r0,#1
	ldr r1,=msg3
	mov r2,#17
	mov r7,#4
	swi #0

	b menu  @se carga label de menu

mensaje4:@cuarto label de mensajes
	mov r0,#1
	ldr r1,=msg4
	mov r2,#34
	mov r7,#4
	swi #0

	b menu  @se carga label de menu

mensaje5:@quinto label de mensajes
	mov r0,#1
	ldr r1,=msg5
	mov r2,#17
	mov r7,#4
	swi #0

	mov r0,#0
        ldr r1, =mensajeU
        mov r2, #256
        mov r7, #3
        swi #0

	mov r0, #1
	ldr r1, =mensajeU
	mov r2,#256
	mov r7, #4
	swi #0


	b menu  @se carga label de menu

salir:@ label para salir
    @se pone los registros en 0
	mov r0,#0 
	pop {r7,lr} @se elimina el push para liberar el programa
	bx lr @se interrumpe el programa para cerrar
	
