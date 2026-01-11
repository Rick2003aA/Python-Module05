/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rtsubuku <rtsubuku@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/14 14:11:12 by rtsubuku          #+#    #+#             */
/*   Updated: 2025/08/21 11:49:58 by rtsubuku         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	f;
	int	i;
	int	j;

	if (nb < 0)
	{
		return (0);
	}
	f = 1;
	i = 1;
	j = 0;
	while (j < nb)
	{
		f = f * i;
		i++;
		j++;
	}
	return (f);
}

// #include <stdio.h>
// int	main(void)
// {
// 	printf("%d", ft_iterative_factorial(3));
// }
