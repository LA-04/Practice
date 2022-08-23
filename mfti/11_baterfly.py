puts 'Введите количество аргументов:'
n = gets.chomp
n = n.to_i

rand = true
puts 'Вы хотите заполнить таблицу истинности вручную? [y/n]'
rand = false if gets.chomp == 'y'

matrix = []
(2**n).times do |i|
  tmp = ("%0#{n}b" % i).split('')
  res = []
  tmp.each { |t| res << t.to_i }
  if rand
    x = Random.rand(0..1).round
  else
    puts "Введите x#{i + 1}:"
    x = gets.chomp.to_i
  end
  res << x
  matrix[i] = res
end

puts 'Полученная таблица истинности:'
matrix.each do |j|
  puts j.inspect
end

# СКНФ
# 1) Для нахождения СКНФ нужно из таблицы истинности выделить лишь те строки
# , результат которых равен 0
# если значение переменной в данной строке равно 0,
# то в дизъюнкцию записываем саму переменную,
# а если равно 1,
# то - отрицание этой переменной.
# После этого все дизъюнкции связываем в конъюнкцию.

OR = 'V'
AND = '*'
WORD = 'a'
MINUS = '-'

result = ''
matrix.each do |line|
  if line.last == 0
    args = line.clone
    args.pop
    word = WORD
    args.each_with_index do |var, index|
      word = word.next if index > 0
      if var == 0
        append = ''
        append += OR if index > 0
        append += word
        result << append
      elsif var == 1
        append = ''
        append += OR if index > 0
        append += MINUS
        append += word
        result << append
      end
    end
    result += AND
  end
end

result[result.length - 1] = '' if result[result.length - 1] == AND

puts "\nСКНФ:"
puts result
puts 'Так как все значения в таблице истинности равны 1, то данная функция не имеет СКНФ.' if result.empty?

# СДНФ
# Для нахождения СДНФ нужно из таблицы истинности выделить лишь те строки,
# результат которых равен 1.
# Далее, для каждой строки выписываем конъюнкцию всех переменных
# по следующему алгоритму:
# если значение переменной в данной строке равно 1,
# то в конъюнкцию записываем саму переменную,
# а если равно 0,
# то - отрицание этой переменной.
# После этого все конъюнкции связываем в дизъюнкцию.

result = ''
matrix.each do |line|
  if line.last == 1
    args = line.clone
    args.pop
    word = WORD
    args.each_with_index do |var, index|
      word = word.next if index > 0
      if var == 1
        append = ''
        append += AND if index > 0
        append += word
        result << append
      elsif var == 0
        append = ''
        append += AND if index > 0
        append += MINUS
        append += word
        result << append
      end
    end
    result += OR
  end
end

result[result.length - 1] = '' if result[result.length - 1] == OR

puts "\nСДНФ:"
puts result
puts 'Так как все значения в таблице истинности равны 0, то данная функция не имеет СДНФ.' if result.empty?

# n - args count
puts "\n\n" if matrix[0].count == n + 1
puts "Тест 1 пройден" if matrix[0].count == n + 1
puts "Тест 2 пройден" if matrix.count == 2**n