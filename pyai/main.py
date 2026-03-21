## importar módulo completo

#import fibonacci as fib

#print(fib.enesimo_fib(2))
#print(fib.sequencia_fib(10))
#print(fib.estimar_prop_aurea(10))

#print(fib.__name__)

## importar funcoes especificas
from fibonacci import enesimo_fib, sequencia_fib

enesimo = enesimo_fib(2)
seq = sequencia_fib(10)

print(enesimo)
print(seq)