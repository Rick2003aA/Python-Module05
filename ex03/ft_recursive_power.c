/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rtsubuku <rtsubuku@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/14 20:04:55 by rtsubuku          #+#    #+#             */
/*   Updated: 2025/08/21 12:10:31 by rtsubuku         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_power(int nb, int power)
{
	if (power == 0)
	{
		return (1);
	}
	nb = nb * ft_recursive_power(nb, power - 1);
	return (nb);
}

// #include <stdio.h>
// int	main(void)
// {
// 	printf("%d", ft_recursive_power(10, 2));
// }
