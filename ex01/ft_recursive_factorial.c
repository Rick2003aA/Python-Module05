/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rtsubuku <rtsubuku@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/14 14:11:12 by rtsubuku          #+#    #+#             */
/*   Updated: 2025/08/21 12:08:22 by rtsubuku         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_factorial(int nb)
{
	if (nb < 0)
		return (0);
	if (nb == 0)
	{
		return (1);
	}
	nb = nb * ft_recursive_factorial(nb - 1);
	return (nb);
}

// #include <stdio.h>
// int	main(void)
// {
// 	printf("%d", ft_recursive_factorial(3));
// }
