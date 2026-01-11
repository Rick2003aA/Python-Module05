/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rtsubuku <rtsubuku@student.42tokyo.jp>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/20 08:03:02 by rtsubuku          #+#    #+#             */
/*   Updated: 2025/08/21 12:30:24 by rtsubuku         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_sqrt(int nb)
{
	int	nb2;

	if (nb < 0)
		return (0);
	nb2 = 1;
	while (nb2 <= nb / nb2)
	{
		if (nb2 * nb2 == nb)
			return (nb2);
		nb2++;
	}
	return (0);
}

// #include <stdio.h>
// #include <limits.h>
// int	main(void)
// {
// 	int	i;

// 	i = INT_MAX -100;
// 	while (i < INT_MAX)
// 	{
// 		printf("%d", ft_sqrt(i));
// 		i++;
// 	}
// }
