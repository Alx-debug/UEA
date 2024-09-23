def calcular_descuento(monto_total, porcentaje_descuento=10):
  """
  Calcula el monto del descuento en base al monto total y el porcentaje de descuento.

  Args:
      monto_total: El monto total de la compra.
      porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto 10%).

  Returns:
      El monto del descuento calculado.
  """
  descuento = (porcentaje_descuento / 100) * monto_total
  return descuento

# Llamadas a la función
monto_compra1 = 150
descuento1 = calcular_descuento(monto_compra1)  # Usando el descuento por defecto (10%)
monto_final1 = monto_compra1 - descuento1

monto_compra2 = 200
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

# Mostrar resultados
print(f"Compra 1: Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")
print(f"Compra 2: Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")
