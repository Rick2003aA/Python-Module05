/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_fibonacci.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rtsubuku <rtsubuku@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/20 07:55:05 by rtsubuku          #+#    #+#             */
/*   Updated: 2025/08/21 12:30:46 by rtsubuku         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_fibonacci(int index)
{
	if (index < 0)
		return (-1);
	if (index == 0)
		return (0);
	if (index == 1)
		return (1);
	index = ft_fibonacci(index - 2) + ft_fibonacci(index - 1);
	return (index);
}

// #include <stdio.h>
// int	main(void)
// {
// 	printf("%d", ft_fibonacci(0));
// 	printf("%d", ft_fibonacci(1));
// 	printf("%d", ft_fibonacci(2));
// 	printf("%d", ft_fibonacci(3));
// 	printf("%d", ft_fibonacci(4));
// 	printf("%d", ft_fibonacci(5));
// }
